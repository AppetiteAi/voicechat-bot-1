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

from db.mongodbhandler import MongoDBHandler

mongo_handler = MongoDBHandler()
mongo_handler2 = MongoDBHandler()
mongo_handler3 = MongoDBHandler()
assert mongo_handler is mongo_handler2 and mongo_handler2 is mongo_handler3
print("MongoDBHandler instance created successfully")
