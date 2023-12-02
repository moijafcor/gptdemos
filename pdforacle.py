# pdforacle.py

import sys
import os
import dotenv
from langchain_experimental.pal_chain.base import PALChain
from langchain.llms import HuggingFaceHub
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

dotenv.load_dotenv()


def main():
    print("Hello world!")


if __name__ == "__main__":
    main()
