# chatbot_tokens_counter.py
import sys
import os
import argparse
from openai import OpenAI
import dotenv
from bin.token_counter import num_tokens_from_string

dotenv.load_dotenv()


def main(
    personality: str = "You are a sweet old helpful grandma",
    openai_llm_model_name: str = "gpt-3.5-turbo",
    verbose: str = "yes",
) -> None:
    """
    quit, exit, or bye to exit the program

    A function that simulates a conversation between a user and a GPT personality using OpenAI's LLM_MODEL.

    The function initializes the conversation with a system message and then enters a loop where it prompts the user for input,
    sends the user's message along with the conversation history to the GPT-3.5 Turbo LLM_MODEL for generating a response from the grandma,
    and prints the grandma's response. The conversation history is updated with the user's message and the grandma's response.

    The function also calculates the total number of tokens in the conversation history and prints it.

    Note: The function requires the OpenAI API key to be set as an environment variable named "OPENAI_API_KEY".

    Args:
        personality (str): The initial system message representing the personality of the grandma. Defaults to "You are a sweet old helpful grandma".
        openai_llm_model_name (str): The name of the OpenAI LLM_MODEL to use. Defaults to "gpt-3.5-turbo".
        verbose (str): Toggles printing message information and stats.

    Returns:
        None
    """
    # Initialize conversation with a system message
    messages = []
    total_tokens = []
    tuning = {"role": "system", "content": personality}
    # This list is incomplete. Add more models as they become available.
    supported_openai_models = ["gpt-4", "gpt-3.5-turbo", "text-embedding-ada-002"]
    if openai_llm_model_name not in supported_openai_models:
        print(
            "Invalid OpenAI model name. Please choose from: ", supported_openai_models
        )
        sys.exit()
    else:
        llm_model = openai_llm_model_name

    # @see https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    encoding_name = "cl100k_base"

    if verbose == "yes" or verbose == "y":
        is_verbose = True
    else:
        is_verbose = False

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    messages.append(tuning)
    print(f"System: {personality}")

    while True:
        user_text = input("User: ")

        if user_text == "quit" or user_text == "exit" or user_text == "bye":
            sys.exit()

        # Add the user message to the conversation history
        messages.append({"role": "user", "content": user_text})

        response = client.chat.completions.create(
            messages=messages,
            model=llm_model,
        )

        chatbot_response = response.choices[0].message.content
        if is_verbose is True:
            print("***")

        # Add chatbot message to the conversation history
        messages.append({"role": "assistant", "content": chatbot_response})

        for i, message in enumerate(messages):
            if is_verbose is True:
                print(f"{i} - {message['role']}: {message['content']}")
                total_tokens.append(
                    num_tokens_from_string(message["content"], encoding_name)
                )
            else:
                print(f"{message['role']}: {message['content']}")

        if is_verbose is True:
            print(f"Tokens: {sum(total_tokens)}")
            print("***")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="chatbot_tokens_counter.py",
        description="A script that simulates a conversation between a user and a GPT personality using OpenAI's LLM_MODEL.",
        epilog="Type quit, exit, or bye to exit the program",
    )
    parser.add_argument(
        "-p",
        "--personality",
        type=str,
        default="You are a sweet old helpful grandma",
        help="The initial system message representing the personality of the grandma. Defaults to 'You are a sweet old helpful grandma'.",
    )
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="gpt-3.5-turbo",
        choices=["gpt-4", "gpt-3.5-turbo", "text-embedding-ada-002"],
        help="The name of the OpenAI LLM_MODEL to use. Defaults to 'gpt-3.5-turbo'.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        type=str,
        default="yes",
        choices=["yes", "no", "y", "n"],
        help="Toggles printing message information and stats.",
    )
    args = parser.parse_args()
    main(
        personality=args.personality,
        openai_llm_model_name=args.model,
        verbose=args.verbose.lower(),
    )
