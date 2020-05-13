# app/mongo_queries.py

import pymongo
import os
from dotenv import load_dotenv

# Load info from .env file
load_dotenv()

# Set up .env variables to connect to MongoDB
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

# Set connection to MongoDB
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
print(dir(client))
print("DB NAMES:", client.list_database_names)

db = client.ds14_db # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.rpg # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    "fav_icecream_flavors":["vanilla", "choc"],
    "stats":{"a":1,"b":2,"c":[1,2,3]},
    })
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))