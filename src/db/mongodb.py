import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']
client = MongoClient(MONGODB_URI)
db = client['RifasVivi']  # Use o nome do seu banco

