import datetime

class Question():
    author: str
    text: str
    date: datetime.date

    def __init__(self, author, text) -> None:
        self.author = author
        self.text = text
        self.date = datetime.date.today()

    def asdict(self):
        return {'author': self.author, 'text': self.text, 'date': str(self.date)}