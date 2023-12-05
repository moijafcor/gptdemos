# marketer.py


import sys
import os
import dotenv
from langchain_experimental.pal_chain.base import PALChain
from langchain.llms import HuggingFaceHub
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

dotenv.load_dotenv()

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")


def main():
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-xxl",
        model_kwargs={"temperature": 0.5, "max_length": 512},
    )

    # Initialize conversation with a system message
    messages = [{"role": "system", "content": "You are a sweet old helpful grandma."}]

    while True:
        user_text = input("Bucky: ")

        # Add the user message to the conversation history
        messages.append({"role": "user", "content": user_text})

        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo", messages=messages, temperature=0.5, max_tokens=1024
        # )

        response = llm.

        granny_response = response.choices[0].message.content
        print(f"Granny: {granny_response}")

        # Add grandmas message to the conversation history
        messages.append({"role": "assistant", "content": granny_response})


if __name__ == "__main__":
    main()
