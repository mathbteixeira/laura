from dotenv import load_dotenv
from pathlib import Path
import os
import pymongo
import pandas as pd
import json

# Loading configs
env_path = Path('.') / 'env_file.env'
load_dotenv(dotenv_path=env_path)
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD= os.getenv("DATABASE_PASSWORD")
ATLAS_CONNECTION_STRING = os.getenv("ATLAS_CONNECTION_STRING")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
CSV_PATH = os.getenv("CSV_PATH")

# Connecting to DB
myclient = pymongo.MongoClient("mongodb+srv://"+DATABASE_USER+":"+DATABASE_PASSWORD+"@"+ATLAS_CONNECTION_STRING)
mydb = myclient[DATABASE_NAME]
mycol = mydb[COLLECTION_NAME]

# Importing CSV data
data = pd.read_csv(CSV_PATH)
payload = json.loads(data.to_json(orient='records'))
mycol.delete_many({})
mycol.insert_many(payload)

print("Data import was successfull.")