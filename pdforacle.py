# pdforacle.py

import dotenv
from langchain.chains import LLMChain
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain_experimental.pal_chain.base import PALChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import (
    # Role the Bot should act as
    SystemMessage,
    HumanMessage,
    AIMessage,
)
from langchain.vectorstores import FAISS
import os
from PyPDF2 import PdfReader
import streamlit as st
from streamlit_chat import message
import sys


def scaffold() -> None:
    st.set_page_config(
        page_title="PDF Oracle | Inspired on ChatGPT", page_icon=":grin:"
    )
    st.header("PDF Oracle :grin:")
    st.text_input("Query your PDFs:")


def get_pdf_stream(pdf_files):
    stream = ""
    for pdf in pdf_files:
        pdf_reader = PdfReader(pdf)
        for chunk in pdf_reader.pages:
            stream += chunk.extract_text()
    return stream


def chunker(stream):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    return splitter.split_text(stream)


def vectordb(chunk):
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    return FAISS.from_texts(texts=chunk, embedding=embeddings)


def main() -> None:
    scaffold()
    dotenv.load_dotenv()

    message("Hello!")
    message("All good", is_user=True)

    with st.sidebar:
        st.subheader("Your PDFs Collection")
        pdf_raw = st.file_uploader(
            "Please upload PDFs and hit 'Process'", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Working"):
                pdf_stream = get_pdf_stream(pdf_raw)
                chunks = chunker(pdf_stream)
                # st.write(chunks)
                vectorstore = vectordb(chunks)


if __name__ == "__main__":
    main()
