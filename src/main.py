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
    question = api.getQuestion(id)

    if question == 404:
        return flask.redirect("/404")
    else:
        return flask.render_template("view_question.html", subject = question.subject, text = question.text, date = question.date)

@app.route("/404")
def notfound():
    return flask.render_template("404.html")

@app.route("/postAnswer", methods = [ 'POST' ])
def postAnswer():
    text = flask.request.form.get('text')
    question = flask.request.form.get('question')

    api.addAnswer(question, text)
    
    return flask.redirect("/question/" + str(question))

if __name__ == '__main__':
    app.run()