import flask
import api

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/post", methods = ['GET'])
def postQuestion():
    author = flask.request.args['author']
    text = flask.request.args['text']

    return api.askQuestion(text, author).asdict()

if __name__ == '__main__':
    app.run()