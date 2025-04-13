from dotenv import load_dotenv
import os
from pymongo import MongoClient
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
ROUTE_TABLE = os.getenv("ROUTE_TABLE")
STOP_BUS = os.getenv("STOP_BUS")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
route_table = db[ROUTE_TABLE]
stop_bus = db[STOP_BUS]


# Helper to convert ObjectId to string
def serialize_out(bus):
    bus["_id"] = str(bus["_id"])
    return bus