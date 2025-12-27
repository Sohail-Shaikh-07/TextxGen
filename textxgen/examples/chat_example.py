from textxgen import ChatEndpoint


def chat_example():
    """ 
    Example of using the TextxGen chat endpoint.
    """
    # Initialize the chat endpoint
    chat = ChatEndpoint()

    # Example 1: Simple chat completion
    print("Example 1: Simple Chat Completion")
    print("-" * 50)

    messages = [{"role": "user", "content": "What is artificial intelligence?"}]
    response = chat.chat(
        messages=messages,
        model="grok4.1_fast",
        temperature=0.7,
        max_tokens=100,
    )
    print("User: What is artificial intelligence?")
    print(f"AI: {response}\n")

    # Example 2: Chat with system prompt
    print("Example 2: Chat with System Prompt")
    print("-" * 50)

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."},
    ]
    response = chat.chat(
        messages=messages,
        model="grok4.1_fast",
        temperature=0.7,
        max_tokens=150,
        raw_response=True,
    )
    print("User: Explain quantum computing in simple terms.")
    print(f"AI: {response}\n")

    # Example 3: Streaming chat completion
    print("Example 3: Streaming Chat Completion")
    print("-" * 50)

    messages = [{"role": "user", "content": "Write a short story about a robot."}]
    print("User: Write a short story about a robot.")
    print("AI: ", end="", flush=True)
    for content in chat.chat(
        messages=messages,
        model="grok4.1_fast",
        temperature=0.8,
        max_tokens=100,
        stream=True,
    ):
        print(content, end="", flush=True)
    print("\n")


if __name__ == "__main__":
    chat_example()
