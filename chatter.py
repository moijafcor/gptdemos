# chatter.py
import os
import argparse
from openai import OpenAI
import dotenv
from token_counter import num_tokens_from_string

dotenv.load_dotenv()


def chatter(
    personality: str = "You are a sweet old helpful grandma",
    openai_llm_model_name: str = "gpt-3.5-turbo",
    verbose: str = "Yes",
) -> None:
    """
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
    llm_model = openai_llm_model_name
    encoding_name = "cl100k_base"

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    while True:
        messages.append(tuning)
        user_text = input("User: ")

        # Add the user message to the conversation history
        messages.append({"role": "user", "content": user_text})

        response = client.chat.completions.create(
            messages=messages,
            model=llm_model,
        )

        chatbot_response = response.choices[0].message.content
        if verbose == "Yes":
            print(f"Chatbot: {chatbot_response}")
            print("***")

        # Add grandmas message to the conversation history
        messages.append({"role": "assistant", "content": chatbot_response})

        for i, message in enumerate(messages):
            print(f"{i} - {message['role']}: {message['content']}")
            total_tokens.append(
                num_tokens_from_string(message["content"], encoding_name)
            )

        total_tokens_2 = sum(total_tokens)
        if verbose == "Yes":
            print(f"Tokens: {total_tokens_2}")
            print("***")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--personality",
        type=str,
        default="You are a sweet old helpful grandma",
        help="The initial system message representing the personality of the grandma. Defaults to 'You are a sweet old helpful grandma'.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-3.5-turbo",
        help="The name of the OpenAI LLM_MODEL to use. Defaults to 'gpt-3.5-turbo'.",
    )
    parser.add_argument(
        "--verbose",
        type=str,
        default="Yes",
        help="Toggles printing message information and stats.",
    )
    args = parser.parse_args()
    chatter(
        personality=args.personality,
        openai_llm_model_name=args.model,
        verbose=args.verbose,
    )
