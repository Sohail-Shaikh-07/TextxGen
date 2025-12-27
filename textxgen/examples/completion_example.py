from textxgen.endpoints.completions import CompletionsEndpoint


def completion_example():
    """
    Example of using the TextxGen completion endpoint with different response formats.
    """
    # Initialize the completion endpoint
    completions = CompletionsEndpoint()

    # Example 1: Normal formatted response (default)
    print("Example 1: Normal Formatted Response")
    print("-" * 50)
    prompt = "Write a haiku about nature:"
    response = completions.complete(
        prompt=prompt,
        model="grok4.1_fast",
        temperature=0.7,
        max_tokens=50,
    )
    print(f"Prompt: {prompt}")
    print(f"Completion: {response}\n")

    # Example 2: Raw JSON response
    print("Example 2: Raw JSON Response")
    print("-" * 50)
    prompt = "Write a short story about a robot:"
    response = completions.complete(
        prompt=prompt,
        model="grok4.1_fast",
        temperature=0.7,
        max_tokens=100,
        raw_response=True,  # Get raw JSON response
    )
    print(f"Prompt: {prompt}")
    print("Raw Response:")
    print(response)
    print("\n")

    # Example 3: Streaming response
    print("Example 3: Streaming Response")
    print("-" * 50)
    prompt = "Write a poem about technology:"
    print(f"Prompt: {prompt}")
    print("Completion: ", end="", flush=True)
    for content in completions.complete(
        prompt=prompt,
        model="grok4.1_fast",
        temperature=0.8,
        max_tokens=100,
        stream=True,
    ):
        print(content, end="", flush=True)
    print("\n")

    # Example 4: Multiple completions with raw response
    print("Example 4: Multiple Completions (Raw)")
    print("-" * 50)
    prompt = "Give me three different ways to say 'hello':"
    response = completions.complete(
        prompt=prompt,
        model="grok4.1_fast",
        temperature=0.9,
        max_tokens=50,
        n=3,
        raw_response=True,  # Get raw JSON response
    )
    print(f"Prompt: {prompt}")
    print("Raw Response:")
    print(response)
    print("\n")

    # Example 5: Completion with stop sequences
    print("Example 5: Completion with Stop Sequences")
    print("-" * 50)
    prompt = "Once upon a time,"
    response = completions.complete(
        prompt=prompt,
        model="grok4.1_fast",
        temperature=0.8,
        max_tokens=100,
        stop=["The End", "END"],
        top_p=0.9,
    )
    print(f"Prompt: {prompt}")
    print(f"Completion: {response}\n")


if __name__ == "__main__":
    completion_example()