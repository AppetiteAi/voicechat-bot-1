from flask import Blueprint, jsonify, request
from db.mongodb_handler import MongoDBHandler

restaurant_bp = Blueprint("restaurant", __name__)
mongodb = MongoDBHandler()
restaurants_collection = mongodb.get_database().get_collection("Restaurants")

@restaurant_bp.route("/ping", methods=["GET"]) #Test method to check if the server is running
def ping():
    return "pong"

@restaurant_bp.route("/get_information", methods=["GET"]) #Gets all of restaurant's information in json format given name
def get_information():
    restaurant_name = request.args.get('name')
    if not restaurant_name:
        return jsonify({"error": "restaurant's name not provided"}), 400
    
    mongo_handler = MongoDBHandler()
    target_restaurant = (
        mongo_handler.get_database()
        .get_collection("Restaurants")
        .find_one({"name": restaurant_name})
    )

    if not target_restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    # Remove the _id field
    target_restaurant.pop('_id', None)
    target_restaurant.pop('updated_at', None)
    target_restaurant.pop('name', None)

    return jsonify({"restaurant": target_restaurant}), 200

@restaurant_bp.route("/list_restaurants", methods=["GET"]) #Lists all restaurant names in the database
def list_restaurants():
    mongo_handler = MongoDBHandler()
    restaurants = (
        mongo_handler.get_database()
        .get_collection("Restaurants")
        .find({}, {"name": 1, "_id": 0})
    )

    restaurant_names = [restaurant["name"] for restaurant in restaurants]

    return jsonify({"restaurant_names": restaurant_names}), 200