import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db.testcollection

post = {"author": "John",
        "text": "Just a test",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id

