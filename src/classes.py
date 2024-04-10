import datetime

class Question():
    text: str
    date: datetime.date
    subject: str

    def __init__(self,text, subject, date = None) -> None:
        self.text = text
        
        if date == None:
            self.date = datetime.date.today()
        else:
            format = "%Y-%m-%d"
            self.date = datetime.datetime.strptime(date, format).date()

        self.subject = subject

    def asdict(self):
        return {'text': self.text, 'date': str(self.date), 'subject': self.subject}
    
class Answer():
    text: str
    date: datetime.date
    question: str

    def __init__(self, text, date) -> None:
        self.text = text
        
        if date == None:
            self.date = datetime.date.today()
        else:
            format = "%Y-%m-%d"
            self.date = datetime.datetime.strptime(date, format).date()

        self.question = ""

    def asdict(self):
        return { 'text': self.text, 'date': str(self.date), 'questionID': self.question }