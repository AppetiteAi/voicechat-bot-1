from pymongo import MongoClient
from utils.env_utils import MONGO_ADMIN_USER, MONGO_ADMIN_PASSWORD, MONGO_URL, MONGO_DB

## Sample query
    # query = {'link_path': '/irvins-scrumptious-eats'} #place a restaurant name here
    # restaurant = restaurants.find_one(query)

    # print(restaurant)

    # client.close()

class MongoDBHandler:
    def __init__(self):
        connection_string = f"mongodb+srv://{MONGO_ADMIN_USER}:{MONGO_ADMIN_PASSWORD}@{MONGO_URL}/{MONGO_DB}?retryWrites=true&w=majority"
        self.client = MongoClient(connection_string)
        self.database = self.client.get_database("TablePal")
        self.collection = self.database.get_collection("Restaurants")

    def find_one(self, query):
        return self.collection.find_one(query)

    def find(self, query):
        return self.collection.find(query)

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def update_one(self, query, update):
        return self.collection.update_one(query, update)

    def delete_one(self, query):
        return self.collection.delete_one(query)

    def close(self):
        self.client.close()