import flask
import api

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/post", methods = ['POST'])
def postQuestion():
    text = flask.request.form.get('text')
    subject = flask.request.form.get('subject')
    res = api.askQuestion(text, subject)

    return flask.redirect("/question/" + str(res.inserted_id))

@app.route("/ask")
def draftQuestion():
    return flask.render_template("draft_question.html")

@app.route("/question/<id>")
def question(id):
    return "questions id: " + id

if __name__ == '__main__':
    app.run()