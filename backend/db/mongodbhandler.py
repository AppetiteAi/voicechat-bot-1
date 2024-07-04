import json
import re

import pymongo
from utils.env_utils import MONGO_ADMIN_PASSWORD, MONGO_ADMIN_USER, MONGO_DB, MONGO_URL


class MongoDBHandler:

    # singleton design pattern
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._client = None
        return cls._instance

    def __init__(self):
        if self._client is None:
            self._connect_to_db()

    def _connect_to_db(self):
        connection_string = f"mongodb+srv://{MONGO_ADMIN_USER}:{MONGO_ADMIN_PASSWORD}@{MONGO_URL}/{MONGO_DB}?retryWrites=true&w=majority"
        self._client = pymongo.MongoClient(connection_string)

    def get_database(self):
        if self._client is None:
            raise Exception("MongoDB client has not been initialized for some reason")
        return self._client.get_database("TablePal")

    def translate_validation_error(error):

        error = str(error).replace("'", '"')

        if "E11000" in error:

            pattern = r'"keyValue":\s*({[^}]+})'
            match = re.search(pattern, error)
            key, value = "", ""
            if match:
                key_value = match.group(1)
                key, value = next(iter(json.loads(key_value).items()))

            return {
                "error": (
                    f"Duplicate key error. '{key} : {value}' already exists"
                    if key and value
                    else "Duplicate key error."
                ),
            }

        elif '"operatorName": "required"' in error:
            pattern = r'"missingProperties":\s*\[([^\]]+)\]'
            match = re.search(pattern, error)
            missing_properties = []
            if match:
                missing_properties = match.group(1).split(", ")
                missing_properties = [prop.strip('"') for prop in missing_properties]

            return {
                "error": f"Missing required fields: {missing_properties}",
            }

        elif "type did not match" in error:

            # If it works it works \_('-')_/
            type_error_details = []
            string_to_parse = (
                "{"
                + f"!propertiesNotSatisfied! {error.split('!propertiesNotSatisfied!')[1][0:-4]}"
            ).replace("!", '"')
            properties_not_satisfied = json.loads(string_to_parse)
            for prop in properties_not_satisfied["propertiesNotSatisfied"]:
                prop_name = prop["propertyName"]
                inputted_type = prop["details"][0]["consideredType"]
                expected_type = prop["details"][0]["specifiedAs"]["bsonType"]
                type_error_details.append(
                    {
                        "key": prop_name,
                        "input_type": inputted_type,
                        "expected": expected_type,
                    }
                )
            return {
                "error": f"Invalid data type: {type_error_details}",
            }

        elif "value was not found in enum" in error:

            considered_value_pattern = r'"consideredValue":\s*"([^"]+)"'
            enum_array_pattern = r'"enum":\s*\[([^\]]+)\]'

            considered_value_match = re.search(considered_value_pattern, error)
            considered_value = (
                considered_value_match.group(1) if considered_value_match else None
            )
            enum_array_match = re.search(enum_array_pattern, error)
            enum_array = (
                enum_array_match.group(1).replace('"', "").split(", ")
                if enum_array_match
                else None
            )
            return {
                "error": (
                    f"Invalid enum value: {considered_value}. Expected one of: {enum_array}"
                    if considered_value and enum_array
                    else "Invalid enum value"
                ),
            }
        else:
            return {
                "error": "An error occurred during schema enforcement: " + error,
            }
