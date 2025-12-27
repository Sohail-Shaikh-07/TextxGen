import requests
from typing import Iterator, Dict, Any, Optional
from .exceptions import (
    APIError,
    InvalidInputError,
    NetworkError,
    TimeoutError,
    ConfigurationError,
)
import json
import logging
from .config import Config
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Set up logger
logger = logging.getLogger(__name__)


class APIClient:
    """
    Handles API requests to the proxy server.
    """

    def __init__(self, proxy_url: Optional[str] = None):
        """
        Initialize the client.

        Args:
            proxy_url (str, optional): Custom proxy URL. Defaults to None (uses built-in config).
        """
        self.proxy_url = proxy_url or Config.PROXY_URL

        # Validate proxy URL
        if not self.proxy_url:
            raise ConfigurationError(
                "Proxy URL must be provided either through config or constructor"
            )

        # Set up session with retry logic
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,  # number of retries
            backoff_factor=1,  # wait 1, 2, 4 seconds between retries
            status_forcelist=[500, 502, 503, 504],  # retry on these status codes
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _make_request(
        self,
        endpoint: str,
        method: str = "POST",
        data: dict = None,
        stream: bool = False,
    ) -> Any:
        """
        Makes an API request to the proxy server.

        Args:
            endpoint: API endpoint (e.g., '/chat')
            method: HTTP method (default: POST)
            data: Request payload
            stream: Whether to stream the response

        Returns:
            Parsed JSON response or streaming iterator

        Raises:
            APIError: For request failures
            NetworkError: For network-related issues
            TimeoutError: For timeout issues
        """
        # Construct the full URL
        url = f"{self.proxy_url.rstrip('/')}/{endpoint.lstrip('/')}"

        # Only include content-type header, proxy will handle authentication
        headers = {"Content-Type": "application/json"}

        try:
            logger.debug(f"Making {method} request to proxy: {url}")
            logger.debug(f"Request data: {json.dumps(data, indent=2)}")

            # Use session with retry logic
            response = self.session.request(
                method,
                url,
                json=data,
                stream=stream,
                headers=headers,
                timeout=(10, 300),  # (connect timeout, read timeout)
            )
            response.raise_for_status()

            if stream:
                return self._handle_streaming_response(response)
            return response.json()

        except requests.exceptions.Timeout as e:
            error_msg = f"Request timed out: {str(e)}"
            logger.error(error_msg)
            raise TimeoutError(error_msg) from None

        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP Error: {e.response.status_code} - {e.response.text}"
            logger.error(error_msg)
            raise APIError(error_msg, e.response.status_code) from None

        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection Error: {str(e)}"
            logger.error(error_msg)
            raise NetworkError(error_msg) from None

        except requests.exceptions.RequestException as e:
            error_msg = f"Request Error: {str(e)}"
            logger.error(error_msg)
            raise APIError(
                error_msg, getattr(e.response, "status_code", None)
            ) from None

    def _handle_streaming_response(
        self, response: requests.Response
    ) -> Iterator[Dict[str, Any]]:
        """
        Handles streaming responses from the proxy server.

        Args:
            response: Streaming response object

        Yields:
            Parsed JSON chunks from the stream

        Raises:
            APIError: For parsing failures
        """
        buffer = ""
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                buffer += chunk.decode("utf-8")
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    if line.startswith("data: "):
                        json_data = line[len("data: ") :]
                        if json_data.strip() == "[DONE]":
                            return
                        try:
                            yield json.loads(json_data)
                        except json.JSONDecodeError as e:
                            error_msg = f"JSON Decode Error: {e}"
                            logger.error(error_msg)
                            raise APIError(error_msg, 500) from None

    def chat_completion(
        self,
        messages: list,
        model: str = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        stream: bool = False,
    ) -> Any:
        """
        Sends a chat completion request to the proxy server.

        Args:
            messages: List of chat messages
            model: Model identifier (default: Config.DEFAULT_MODEL)
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            stream: Whether to stream the response

        Returns:
            API response or streaming iterator

        Raises:
            InvalidInputError: For invalid input
            APIError: For API failures
        """
        if not messages or not isinstance(messages, list):
            raise InvalidInputError("Messages must be a non-empty list.")

        payload = {
            "model": model or Config.DEFAULT_MODEL,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream,
        }

        return self._make_request("/chat", data=payload, stream=stream)

    def text_completion(
        self,
        prompt: str,
        model: str = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        stream: bool = False,
        stop: Optional[list] = None,
        n: int = 1,
        top_p: float = 1.0,
    ) -> Any:
        """
        Sends a text completion request to the proxy server.

        Args:
            prompt: Input prompt
            model: Model identifier (default: Config.DEFAULT_MODEL)
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            stream: Whether to stream the response
            stop: Stop sequences
            n: Number of completions
            top_p: Nucleus sampling parameter

        Returns:
            API response or streaming iterator

        Raises:
            InvalidInputError: For invalid input
            APIError: For API failures
        """
        if not prompt or not isinstance(prompt, str):
            raise InvalidInputError("Prompt must be a non-empty string.")

        # Convert prompt to chat format for OpenRouter
        messages = [{"role": "user", "content": prompt}]

        payload = {
            "model": model or Config.DEFAULT_MODEL,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream,
            "stop": stop,
            "n": n,
            "top_p": top_p,
        }

        return self._make_request("/chat", data=payload, stream=stream)
