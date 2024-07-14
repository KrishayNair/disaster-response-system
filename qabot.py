from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display # type: ignore
from IPython.display import Markdown # type: ignore
from langflow import load_flow_from_json 


TWEAKS = {
  "PyPDFLoader-meyB2": {},
  "RecursiveCharacterTextSplitter-aIe6R": {},
  "OllamaEmbeddings-FzJxP": {},
  "BaseChatModel-uQUH3": {},
  "ConversationBufferMemory-adobv": {},
  "ConversationalRetrievalChain-RD8zz": {},
  "FAISS-I7M5T": {},
  "PyPDFLoader-BqluX": {},
  "PyPDFLoader-wBYkk": {},
  "PyPDFLoader-cvTr4": {}
}


def run_flow(inputs: dict, flow_id: str, tweaks: Optional[dict] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param flow_id: The ID of the flow to run
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/{FLOW_ID}"

    payload = {"inputs": inputs}
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()



def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Disaster ChatBot using Langflow")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)