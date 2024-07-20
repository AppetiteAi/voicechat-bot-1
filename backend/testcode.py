from dotenv import load_dotenv
from utils.env_utils import OPEN_AI_KEY, OPEN_AI_MODEL, MONGO_ADMIN_USER, MONGO_ADMIN_PASSWORD, MONGO_URL, MONGO_DB

# Print out the values to verify they are correct
print("OpenAI Key:", OPEN_AI_KEY)
print("OpenAI Model:", OPEN_AI_MODEL)
print("MongoDB User:", MONGO_ADMIN_USER)
print("MongoDB Password:", MONGO_ADMIN_PASSWORD)
print("MongoDB URL:", MONGO_URL)
print("MongoDB Database:", MONGO_DB)

# Testing the MongoDBHandler class

from db.mongodb_handler import MongoDBHandler

mongo_handler = MongoDBHandler()
target_restaurant = (
    mongo_handler
    .get_database()
    .get_collection("Restaurants")
    .find_one({"link_path": "/irvins-scrumptious-eats"})
)
print(target_restaurant)
# query = {'link_path': '/irvins-scrumptious-eats'} #place a restaurant name here
    # restaurant = restaurants.find_one(query)
print("MongoDBHandler instance created successfully")
