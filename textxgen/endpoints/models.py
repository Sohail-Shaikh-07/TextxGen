# textxgen/endpoints/models.py

from ..models import Models

class ModelsEndpoint:
    """
    Handles model-related interactions.
    """

    def __init__(self):
        self.models = Models()

    def list_models(self) -> dict:
        """
        Returns a dictionary of all supported models (actual model IDs).

        Returns:
            dict: Supported models.
        """
        return self.models.list_models()

    def list_display_models(self) -> dict:
        """
        Returns a dictionary of all supported models (display names).

        Returns:
            dict: Supported models with display names.
        """
        return self.models.list_display_models()

    def get_model(self, model_name: str) -> str:
        """
        Retrieves the model ID for a given model name.

        Args:
            model_name (str): Name of the model (e.g., "llama3", "phi3").

        Returns:
            str: Model ID.

        Raises:
            ModelNotSupportedError: If the model is not supported.
        """
        return self.models.get_model(model_name)