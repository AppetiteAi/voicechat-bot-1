from vapi_python import Vapi
from dotenv import load_dotenv
import os
import sys
from testcode2 import generate_text

try:
    # Load environment variables from .env file
    load_dotenv()

    # Get API keys from environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")
    vapi_api_key = os.getenv("VAPI_API_KEY")

    # Ensure both API keys are provided
    if not openai_api_key or not vapi_api_key:
        raise ValueError("API key(s) not found. Please check your .env file or environment variables.")

    # Initialize Vapi AI instance
    vapi_instance = Vapi(vapi_api_key)

    assistant = {
        'firstMessage': 'Hey, how are you?',
        'context': 'You are an employee at a drive thru...',
        'model': 'gpt-3.5-turbo',
        'voice': 'jennifer-playht',
        "recordingEnabled": True,
        "interruptionsEnabled": False
    }

    vapi_instance.start(assistant=assistant)

    # Get user query from command line arguments
    query = sys.argv[1]

    # Generate text using OpenAI's model
    generated_text = generate_text(query, openai_api_key)

    # Pass generated text to Vapi AI
    vapi_response = vapi_instance.query(generated_text)

    # Print Vapi AI response
    print(vapi_response)

except Exception as e:
    print(f"An error occurred: {e}")
