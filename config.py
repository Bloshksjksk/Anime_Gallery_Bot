import os
import dotenv
from telethon import TelegramClient
from pymongo import MongoClient
from API.gogoanimeapi import Gogo
from pymongo.collection import Collection

dotenv.load_dotenv(".env")

api_id = os.environ.get('API_ID','4682685')
api_hash = os.environ.get('API_HASH','3eba5d471162181b8a3f7f5c0a23c307')
bot_token = os.environ.get('BOT_TOKEN','6017558004:AAHaJLg-IaYE-yvj9lFV_7hMqIPuvSt8ihg')
db_url = os.environ.get('MONGO_DB_URL','mongodb+srv://misoc51233:v3pG5FQRUgXCTSXr@cluster0.g19g3z3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
database_name = os.environ.get('DATABASE_NAME','aniecollection')
owner_id = int(os.environ.get('OWNER_ID','945284066'))
bot_username = os.environ.get('BOT_USERNAME','AnimeSearchTb_Bot')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client = MongoClient(db_url, tls=True)
data = Collection(client[database_name], 'ConfigDB').find_one({"_id":"GogoAnime"})

gogo = Gogo(
        gogoanime_token=data["gogoanime"],
        auth_token=data["auth"],
        host=data["url"]
    )
