from textxgen.endpoints.chat import ChatEndpoint
from textxgen.endpoints.completions import CompletionsEndpoint


def simple_example():
    """
    Simple example showing automatic response formatting.
    """
    # Initialize endpoints
    chat = ChatEndpoint()
    completions = CompletionsEndpoint()

    # Chat example - response is automatically formatted
    print("Chat Example:")
    print("-" * 30)
    chat_response = chat.chat(
        messages=[{"role": "user", "content": "Tell me a joke"}], model="grok4.1_fast", temperature=0.7, max_tokens=100

    )
    print(f"Response: {chat_response}\n")  # Already formatted!

    # Completion example - response is automatically formatted
    print("Completion Example:")
    print("-" * 30)
    completion_response = completions.complete(
        prompt="Write a one-line story", model="grok4.1_fast", temperature=0.7, max_tokens=100
    )
    print(f"Response: {completion_response}\n")  # Already formatted!


if __name__ == "__main__":
    simple_example()
