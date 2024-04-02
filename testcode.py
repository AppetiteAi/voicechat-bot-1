from langchain_openai import ChatOpenAI  # Importing the ChatOpenAI class from the langchain_openai package
from dotenv import load_dotenv
import os

try:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    # Testing API Key
    #print("API Key:", api_key) 

    if not api_key:
        raise ValueError("No API key found. Please check your .env file or environment variables.")

    chat_model = ChatOpenAI(openai_api_key=api_key)

    result = chat_model.invoke("Hi")
    print(result.content)
except Exception as e:
    print(f"An error occurred: {e}")
