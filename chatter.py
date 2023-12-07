import os
from openai import OpenAI
import dotenv
from token_counter import num_tokens_from_string

dotenv.load_dotenv()

# Initialize conversation with a system message
messages = []
total_tokens = []
tuning = {"role": "system", "content": "You are a sweet old helpful grandma."}
MODEL = "gpt-3.5-turbo"
ENCODING_NAME = "cl100k_base"

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

while True:
    messages.append(tuning)
    user_text = input("User: ")

    # Add the user message to the conversation history
    messages.append({"role": "user", "content": user_text})

    # print(messages)
    # total_tokens_1 = num_tokens_from_string(messages[0]["content"], ENCODING_NAME)
    # print(f"Tokens: {total_tokens_1}")

    response = client.chat.completions.create(
        messages=messages,
        model=MODEL,
    )

    granny_response = response.choices[0].message.content
    print(f"Granny: {granny_response}")

    # Add grandmas message to the conversation history
    messages.append({"role": "assistant", "content": granny_response})

    print(messages)
    for i, message in enumerate(messages):
        if i % 2 == 0:
            print(f"User: {message['content']}")
            total_tokens.append(
                num_tokens_from_string(message["content"], ENCODING_NAME)
            )
        else:
            print(f"Granny: {message['content']}")
            total_tokens.append(
                num_tokens_from_string(message["content"], ENCODING_NAME)
            )
    total_tokens_2 = sum(total_tokens)
    print(f"Tokens: {total_tokens_2}")
