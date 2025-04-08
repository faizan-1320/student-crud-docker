from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_AUTH_DB = os.getenv("MONGO_AUTH_DB")

MONGO_DETAILS = (
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
    f"{MONGO_DB}?authSource={MONGO_AUTH_DB}"
)

client = MongoClient(MONGO_DETAILS)
database = client[MONGO_DB]
student_collection = database["students"]
