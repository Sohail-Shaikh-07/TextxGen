
from textxgen.endpoints.chat import ChatEndpoint

# Here is the simple chatbot using the textxgen package.

def main():
    """
    Interactive LLM chat application with memory using TextxGen.
    """
    # Initialize the ChatEndpoint
    chat = ChatEndpoint()

    # System prompt to define the AI's behavior
    system_prompt = (
        "Your name is Roxan. You are a helpful, friendly, and knowledgeable assistant. "
        "Your goal is to assist the user with accurate and concise information. "
        "Always maintain a polite and professional tone."
    )

    # Conversation history
    conversation_history = [
        {"role": "system", "content": system_prompt},
    ]

    # Welcome message
    print("Welcome to the LLM Chat! Type 'quit' to exit.\n")

    # Chat loop
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Add the user's message to the conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Send the chat request with streaming
        print("Roxan: ", end="", flush=True)
        response_stream = chat.chat(
            messages=conversation_history,
            model="grok4.1_fast",  # new model
            stream=True,  # Enable streaming
            max_tokens=100,  # Limit response length
            temperature=0.7,  # Adjust creativity
        )

        # Process the streaming response
        roxan_response = ""
        for content in response_stream:
            print(content, end="", flush=True)
            roxan_response += content

        # Add the AI's response to the conversation history
        conversation_history.append({"role": "assistant", "content": roxan_response})

        print("\n")


if __name__ == "__main__":
    main()
