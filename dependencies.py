from pymongo import MongoClient
from pymongo.server_api import ServerApi

from langchain import OpenAI
from dotenv import load_dotenv
import os

#loading the environment variables
load_dotenv()

#loading mongodb connection uri
mongodb_uri = os.getenv("MONGO_DB_URI")

#connecting to MongoDB client
client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# loading our database
db_name = os.getenv("DB")
db = client[db_name]

# loading the names of collections(tables)
collection_cl1_name = os.getenv("COLLECTION_CAT_L1")
collection_cl2_name = os.getenv("COLLECTION_CAT_L2")
collection_val = os.getenv("COLLECTION_VALID")
collection_ticket = os.getenv("COLLECTION_TICKET")
collection_resp = os.getenv("COLLECTION_RESP")

# loading the llms
llm1 = OpenAI(model_name="gpt-3.5-turbo", temperature=0.6)
llm2 = OpenAI(model_name="gpt-3.5-turbo-0301", temperature=0.6)
llm3 = OpenAI(model_name="gpt-3.5-turbo-0613", temperature=0.6)
