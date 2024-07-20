# chat.py
from utils.env_utils import OPEN_AI_KEY, OPEN_AI_MODEL
from db.mongodb_handler import MongoDBHandler
from openai import OpenAI

def mongo_query():
    restaurantCollection = MongoDBHandler()
    query = {'link_path': '/irvins-scrumptious-eats'}
    restaurant = restaurantCollection.find_one(query)
    return restaurant

def query_openai(prompt):
    client = OpenAI(
        api_key=OPEN_AI_KEY
    )
    try:
        response = client.chat.completions.create(
            model=OPEN_AI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return (f"Error querying OpenAI: {e}")

def main():
    restaurant = mongo_query()
    user_input = "Tell me what time this restaurant is open on Wednesdays at its flavor street site and a recommendation a menu item if I like hot and spicy foods"  # Example user query
    combined_query = f"{user_input} {restaurant}"
    response = query_openai(combined_query)

    #For current testing, prints the user input and AI response
    print("User input:", user_input)
    print("AI Response:", response) 

if __name__ == "__main__":
    main()
