from textxgen.endpoints.models import ModelsEndpoint

def main():
    """
    Example usage of the ModelsEndpoint to list and retrieve supported models.
    """
    # Initialize the ModelsEndpoint
    models = ModelsEndpoint()

    # List all supported models
    print("=== Supported Models ===")
    for model_name, display_name in models.list_display_models().items():
        print(f"{model_name}: {display_name}")

if __name__ == "__main__":
    main()