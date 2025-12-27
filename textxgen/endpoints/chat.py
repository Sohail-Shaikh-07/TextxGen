# textxgen/endpoints/chat.py

from typing import Iterator, Dict, Any
from ..client import APIClient
from ..models import Models
from ..exceptions import InvalidInputError
from ..utils import format_api_response


class ChatEndpoint:
    """
    Handles chat-based interactions with the proxy server.
    """

    def __init__(self):
        self.client = APIClient()  # No need to pass proxy_url
        self.models = Models()

    def chat(
        self,
        messages: list,
        model: str = None,
        system_prompt: str = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        stream: bool = False,
        raw_response: bool = False,
    ) -> Any:
        """
        Sends a chat request to the proxy server.

        Args:
            messages (list): List of chat messages
            model (str, optional): Model to use
            system_prompt (str, optional): System prompt to set context
            temperature (float, optional): Sampling temperature
            max_tokens (int, optional): Maximum tokens to generate
            stream (bool, optional): Whether to stream the response
            raw_response (bool, optional): Whether to return raw JSON response

        Returns:
            Union[str, dict, Iterator]: Formatted response, raw JSON, or streaming iterator
        """
        if not messages or not isinstance(messages, list):
            raise InvalidInputError("Messages must be a non-empty list.")

        # Prepare the payload
        payload = {
            "model": self.models.get_model(model) if model else self.models.list_models()["grok4.1_fast"],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream,
        }

        # Add system prompt if provided
        if system_prompt:
            payload["messages"].insert(0, {"role": "system", "content": system_prompt})

        # Send the request
        response = self.client.chat_completion(
            messages=payload["messages"],
            model=payload["model"],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=stream
        )

        if stream:
            def stream_generator():
                for chunk in response:
                    if isinstance(chunk, dict) and "choices" in chunk:
                        choice = chunk["choices"][0]
                        if "delta" in choice and "content" in choice["delta"]:
                            content = choice["delta"]["content"]
                            if content:
                                yield content
            return stream_generator()
        else:
            # Return raw response if requested, otherwise format it
            return response if raw_response else format_api_response(response)

    def get_supported_models_display(self) -> dict:
        """
        Returns a dictionary of supported models with display names.

        Returns:
            dict: Supported models with display names.
        """
        return self.models.list_display_models()
