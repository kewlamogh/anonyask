from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from classes import Question
from bson.objectid import ObjectId

uri = "mongodb+srv://cwaeht2:valistus@dlwork.qoesfcj.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["AnonyAsk"]
col = db["questions"]

def askQuestion(question: str, subject: str):
    question = Question(
        text=question,
        subject=subject
    )
    
    res = col.insert_one(question.asdict())
    return res

def getQuestion(questionID: str):
    doc = col.find_one({ "_id": ObjectId(questionID) })
    q = Question(doc["text"], doc["subject"], doc["date"])

    return q

