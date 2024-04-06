from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from classes import Question, Answer
from bson.objectid import ObjectId

uri = "mongodb+srv://cwaeht2:valistus@dlwork.qoesfcj.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["AnonyAsk"]
questions = db["questions"]
answers = db["answers"]

def askQuestion(question: str, subject: str):
    question = Question(
        text=question,
        subject=subject
    )
    
    res = questions.insert_one(question.asdict())
    return res

def getQuestion(questionID: str):
    doc = questions.find_one({ "_id": ObjectId(questionID) })

    if doc != None:
        q = Question(doc["text"], doc["subject"], doc["date"])
        return q
    else:
        return 404

def addAnswer(questionID: str, answer: Answer):
    answer.question = questionID
    answers.insert_one(answer.asdict())

def getAnswers(questionID: str):
    answers_cursor = answers.find({ "questionID" : questionID})
    answers_list = []

    for doc in answers_cursor:
        print(doc)
        answers_list.append(Answer(doc["text"], doc["date"]))

    return answers_list