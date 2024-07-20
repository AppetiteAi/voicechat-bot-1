from pymongo import MongoClient
from utils.env_utils import MONGO_ADMIN_USER, MONGO_ADMIN_PASSWORD, MONGO_URL, MONGO_DB

## Sample query
    # query = {'link_path': '/irvins-scrumptious-eats'} #place a restaurant name here
    # restaurant = restaurants.find_one(query)

    # print(restaurant)

    # client.close()

class MongoDBHandler:
    
    def __init__(self):
        self._connect_to_db()

    def _connect_to_db(self):
        connection_string = f"mongodb+srv://{MONGO_ADMIN_USER}:{MONGO_ADMIN_PASSWORD}@{MONGO_URL}/{MONGO_DB}?retryWrites=true&w=majority"
        self._client = MongoClient(connection_string)

    def get_database(self):
        if self._client is None:
            raise Exception("MongoDB client has not been initialized for some reason")
        return self._client.get_database("TablePal")