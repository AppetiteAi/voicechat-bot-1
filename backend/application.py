import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import enforce_all_schemas
from routes import blueprints

# Load environment variables
load_dotenv()

# Initialize Flask application
application = Flask(__name__)
CORS(application)

# MongoDB error handling
mongo_error = None
try:
    enforce_all_schemas()
except Exception as e:
    mongo_error = str(e)

# Set the Flask port from environment variable or default to 8000
FLASK_PORT = os.environ.get("FLASK_PORT") or 8000

# Register blueprints
print(os.environ.get("MONGO_ADMIN_USER"))
for bp in blueprints:
    application.register_blueprint(bp, url_prefix=f"/{bp.name}")

# Root route to return JSON
@application.route("/")
def index():
    if mongo_error:
        response = {
            "status": "error",
            "message": "Server connected, but a MONGO error occurred.",
            "error_details": mongo_error,
        }
    else:
        response = {
            "status": "success",
            "message": "Server connected, no MONGO errors detected.",
        }
    return jsonify(response)

if __name__ == "__main__":
    # Run the application with debugging enabled and on the specified port
    application.run(debug=True, port=int(FLASK_PORT))