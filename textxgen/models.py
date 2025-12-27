# textxgen/models.py

from .config import Config
from .exceptions import ModelNotSupportedError


class Models:
    """
    Handles supported models and their validation.
    """

    @staticmethod
    def get_model(model_name: str) -> str:
        """
        Retrieves the model ID for a given model name.

        Args:
            model_name (str): Name of the model (e.g., "llama3", "phi3").

        Returns:
            str: Model ID.

        Raises:
            ModelNotSupportedError: If the model is not supported.
        """
        model_id = Config.SUPPORTED_MODELS.get(model_name.lower())
        if not model_id:
            raise ModelNotSupportedError(model_name)
        return model_id

    @staticmethod
    def list_models() -> dict:
        """
        Returns a dictionary of all supported models (actual model IDs).

        Returns:
            dict: Supported models.
        """
        return Config.SUPPORTED_MODELS

    @staticmethod
    def list_display_models() -> dict:
        """
        Returns a dictionary of all supported models (display names).

        Returns:
            dict: Supported models with display names.
        """
        return Config.get_model_display_names()