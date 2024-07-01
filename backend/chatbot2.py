# chat.py
from utils.env_utils import OPEN_AI_KEY, OPEN_AI_MODEL
from db.mongodbhandler import MongoDBHandler
from openai import ChatCompletion

def fetch_context(database, query):
    collection = database['your_collection_name']  # Adjust the collection name
    document = collection.find_one({"keyword": query})
    return document['context'] if document else query  # Fallback to original query if no context

def query_openai(prompt):
    try:
        response = ChatCompletion.create(
            model=OPEN_AI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            api_key=OPEN_AI_KEY
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error querying OpenAI: {e}")

def main():
    db_handler = MongoDBHandler()
    database = db_handler.get_database()
    user_input = "hello"  # Example user query
    context = fetch_context(database, user_input)
    response = query_openai(context)
    print("Response from OpenAI:", response)

if __name__ == "__main__":
    main()
