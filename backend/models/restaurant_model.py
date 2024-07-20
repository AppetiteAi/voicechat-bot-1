from db.mongodb_handler import MongoDBHandler

restaurant_schema = {
    "bsonType": "object",
    "required": ["name", "background", "tags"],
    "properties": {
        "_id": {"bsonType": "objectId"},
        "name": {"bsonType": "string"},
        "address": {
            "bsonType": "array",  # each item is a separate location
            "items": {"bsonType": "string"},
        },
        "hours": {
            "bsonType": "array",  # index corresponds to index of location in address field
            "items": {
                "bsonType": "object",
                "properties": {
                    "Sunday": {"bsonType": "string"},
                    "Monday": {"bsonType": "string"},
                    "Tuesday": {"bsonType": "string"},
                    "Wednesday": {"bsonType": "string"},
                    "Thursday": {"bsonType": "string"},
                    "Friday": {"bsonType": "string"},
                    "Saturday": {"bsonType": "string"},
                },
            },
        },
        "link_path": {"bsonType": "string"},  # must be unique
        "background": {"bsonType": "string"},
        "menu": {
            "bsonType": "array",
            "items": {
                "bsonType": "object",
                "required": [
                    "_id",
                    "name",
                    "price",
                    "description",
                    "image",
                    "category",
                    "menu_tags",
                    "course_type",
                ],
                "properties": {
                    "_id": {"bsonType": "string"},
                    "name": {"bsonType": "string"},
                    "price": {"bsonType": "string"},
                    "description": {"bsonType": "string"},
                    "image": {"bsonType": "string"},
                    "category": {
                        "bsonType": "array",
                        "items": {"bsonType": "string"},
                    },
                    "menu_tags": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "object",
                            "required": ["weight", "tag"],
                            "properties": {
                                "weight": {
                                    "bsonType": "number",
                                },
                                "tag": {
                                    "bsonType": "string",
                                },
                            },
                        },
                    },
                    "course_type": {
                        "bsonType": "string",
                        "enum": ["appetizer", "entree", "main", "dessert", "drink"],
                    },
                },
            },
        },
        "faq": {
            "bsonType": "array",
            "items": {
                "bsonType": "object",
                "required": ["_id", "question", "answer"],
                "properties": {
                    "_id": {"bsonType": "string"},
                    "question": {"bsonType": "string"},
                    "answer": {"bsonType": "string"},
                },
            },
        },
        "updated_at": {"bsonType": "date"},
        "tags": {
            "bsonType": "array",
            "items": {
                "bsonType": "object",
                "required": ["_id", "tag"],
                "properties": {
                    "_id": {"bsonType": "string"},
                    "tag": {"bsonType": "string"},
                },
            },
        },
    },
    "additionalProperties": False,
}

def enforce_restaurant_schema():
    mongo_handler = MongoDBHandler()
    mongo_handler.get_database().command(
        {
            "collMod": "Restaurants",
            "validator": {"$jsonSchema": restaurant_schema},
            "validationLevel": "strict",
        }
    )
