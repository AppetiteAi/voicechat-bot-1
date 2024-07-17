import re
from datetime import datetime

from bson import ObjectId
from db.mongodb_handler import MongoDBHandler
from flask import Blueprint, jsonify, request

restaurant_bp = Blueprint("restaurant", __name__)
mongodb = MongoDBHandler()
restaurants_collection = mongodb.get_database().get_collection("Restaurants")

@restaurant_bp.route("/get-id/<link_path>", methods=["GET"])
# get restaurant id based off name sent from frontend
def get_id(link_path):
    if not link_path:
        return jsonify({"error": "restaurant's link_path not provided"}), 400
    mongo_handler = MongoDBHandler()
    target_restaurant = (
        mongo_handler.get_database()
        .get_collection("Restaurants")
        .find_one({"link_path": "/" + link_path})
    )
    if not target_restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify({"restaurant_id": str(target_restaurant["_id"])})

# Right now, this endpoint does not work, because you do not have the functionality of the mongodbhandler like giangs code. 
# So, go on google, search up how to connect a mongodb database to your code in PYTHON and try your best to implement it.