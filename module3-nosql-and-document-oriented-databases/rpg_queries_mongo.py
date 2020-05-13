
import pandas as pd
import pymongo
from pymongo import MongoClient
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

db = client.ds14_db # "whatever you want to call it"
print("----------------")
print("DB:", type(db), db)

collection = db.rpg_armory_item # "whatever you want to call it"
print("----------------")
print("COLLECTION:", type(collection), collection)

collection2 = db.rpg_armory_weapon # "whatever you want to call it"
print("----------------")
print("COLLECTION:", type(collection2), collection2)

collection3 = db.rpg_character_inventory # "whatever you want to call it"
print("----------------")
print("COLLECTION:", type(collection3), collection3)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

# Instantiate armory item data
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "armory_item.csv")
df = pd.read_csv(CSV_FILEPATH)
data = df.to_dict(orient='records')
# Add collection to database
collection.insert_many(data)

# Instantiate armory weapon data
CSV_FILEPATH2 = os.path.join(os.path.dirname(__file__), "armory_weapon.csv")
df2 = pd.read_csv(CSV_FILEPATH2)
data2 = df2.to_dict(orient='records')
# Add collection to database
collection2.insert_many(data2)

# Instantiate character inventory data
CSV_FILEPATH3 = os.path.join(os.path.dirname(__file__), "charactercreator_character_inventory.csv")
df3 = pd.read_csv(CSV_FILEPATH3)
data3 = df3.to_dict(orient='records')
# Add collection to database
collection3.insert_many(data3)
