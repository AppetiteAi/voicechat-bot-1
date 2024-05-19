from db.mongodbhandler import MongoDBHandler
from langchain_openai import ChatOpenAI
from utils.env_utils import OPEN_AI_KEY
import sys

def fetch_context(database, collection_name, query):
    collection = database[collection_name]
    document = collection.find_one({"keyword": query})
    return document['context'] if document else "No additional context found."

def main():
    try:
        # Initialize MongoDB Handler
        db_handler = MongoDBHandler()
        database = db_handler.get_database()

        # Get OpenAI API Key
        api_key = OPEN_AI_KEY
        if not api_key:
            raise ValueError("No OpenAI API key found. Please check your environment variables.")

        # Initialize OpenAI Chat model
        chat_model = ChatOpenAI(openai_api_key=api_key)

        # Assume the first argument is the query
        query = sys.argv[1] if len(sys.argv) > 1 else "test"

        # Fetch context from MongoDB
        context = fetch_context(database, "collection_name", query)

        # Combine the original query with the fetched context
        combined_query = f"{query} {context}"
        result = chat_model.invoke(combined_query)
        print(result.content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


