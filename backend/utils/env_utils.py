# env_utils.py
import os
from dotenv import load_dotenv

# Load environment variables from .env
#dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#load_dotenv(dotenv_path)

load_dotenv()

# Export environment variables as constants
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
OPEN_AI_MODEL = os.getenv("OPEN_AI_MODEL")
MONGO_ADMIN_USER = os.getenv("MONGO_ADMIN_USER")
MONGO_ADMIN_PASSWORD = os.getenv("MONGO_ADMIN_PASSWORD")
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")
