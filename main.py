import os
import sys
from dotenv import load_dotenv
import pymongo

load_dotenv()

try:
    client = pymongo.MongoClient(os.getenv("DATABASE_URI"))
    print("success")

except pymongo.errors.ConfigurationError:
    print(
        "An Invalid URI host error was received. Is your Atlas host name correct in your connection string?"
    )
    sys.exit(1)


async def get_database():
    db = client.myDatabase
    return db

# my_collection = db[collection_name]
