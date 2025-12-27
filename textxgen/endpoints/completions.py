# textxgen/endpoints/completions.py

from typing import Iterator, Dict, Any, Optional, List, Union
from ..client import APIClient
from ..models import Models
from ..exceptions import InvalidInputError
from ..utils import format_api_response


class CompletionsEndpoint:
    """
    Handles text completion interactions with OpenRouter models.
    """

    def __init__(self):
        self.client = APIClient()
        self.models = Models()

    def complete(
        self,
        prompt: str,
        model: str = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        stream: bool = False,
        stop: Optional[Union[str, List[str]]] = None,
        n: int = 1,
        top_p: float = 1.0,
        raw_response: bool = False,
    ) -> Any:
        """
        Sends a text completion request to the OpenRouter API.

        Args:
            prompt (str): Input text prompt.
            model (str, optional): Model to use.
            temperature (float, optional): Sampling temperature (default: 0.7).
            max_tokens (int): Maximum number of tokens to generate (default: 1024).
            stream (bool, optional): Whether to stream the response. (default: False).
            stop (Union[str, List[str]], optional): Stop sequences to end generation.
            n (int): Number of completions to generate (default: 1).
            top_p (float): Nucleus sampling parameter (default: 1.0).
            raw_response (bool): Whether to return raw JSON response (default: False).

        Returns:
            Union[str, dict, Iterator]: Formatted response, raw JSON, or streaming iterator

        Raises:
            InvalidInputError: If the prompt is empty or invalid.
        """
        if not prompt or not isinstance(prompt, str):
            raise InvalidInputError("Prompt must be a non-empty string.")

        # Get the model ID from the models list
        model_id = (
            self.models.get_model(model)
            if model
            else self.models.list_models()["grok4.1_fast"]
        )

        # Convert stop to list if it's a string
        if isinstance(stop, str):
            stop = [stop]

        # Use the client's text_completion method
        response = self.client.text_completion(
            prompt=prompt,
            model=model_id,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=stream,
            stop=stop,
            n=n,
            top_p=top_p,
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
