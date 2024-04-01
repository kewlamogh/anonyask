import datetime

class Question():
    author: str
    text: str
    date: datetime.date
    subject: str

    def __init__(self,text, subject) -> None:
        self.text = text
        self.date = datetime.date.today()
        self.subject = subject

    def asdict(self):
        return {'text': self.text, 'date': str(self.date), 'subject': self.subject}