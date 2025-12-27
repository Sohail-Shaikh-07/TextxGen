from textxgen.endpoints.chat import ChatEndpoint
from textxgen.endpoints.completions import CompletionsEndpoint

# Here we have the different examples of chat and completion

def main():
    # Initialize endpoints
    chat = ChatEndpoint()
    completions = CompletionsEndpoint()

    # Example 1: Formatted chat response (default)
    print("Example 1: Formatted Chat Response")
    print("-" * 50)
    messages = [{"role": "user", "content": "What is Python?"}]
    response = chat.chat(
        messages=messages,
        model="grok4.1_fast",
        temperature=0.7,
        max_tokens=100,
    )
    print("User: What is Python?")
    print(f"AI: {response}\n")

    # Example 2: Raw chat response
    print("Example 2: Raw Chat Response")
    print("-" * 50)
    response = chat.chat(
        messages=messages,
        model="grok4.1_fast",
        temperature=0.7,
        max_tokens=100,
        raw_response=True,  # Get raw JSON response
    )
    print("Raw Response:")
    print(response)
    print("\n")

    # Example 3: Formatted completion response (default)
    print("Example 3: Formatted Completion Response")
    print("-" * 50)
    response = completions.complete(
        prompt="Write a one-line story:",
        model="grok4.1_fast",
        temperature=0.7,
        max_tokens=50,
    )
    print(f"Prompt: Write a one-line story:")
    print(f"Completion: {response}\n")

    # Example 4: Raw completion response
    print("Example 4: Raw Completion Response")
    print("-" * 50)
    response = completions.complete(
        prompt="Write a one-line story:",
        model="grok4.1_fast",
        temperature=0.7,
        max_tokens=50,
        raw_response=True,  # Get raw JSON response
    )
    print("Raw Response:")
    print(response)
    print("\n")


if __name__ == "__main__":
    main()
