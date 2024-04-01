from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from classes import Question

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


