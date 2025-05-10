from flask import Flask, render_template

app = Flask(__name__)
# print(__name__)

@app.route("/<username>")
def hello_world(username = None):
    return render_template('index.html', name = username)

@app.route("/blog")
def blog():
    # return ("<p>this is a blog i created</p>")
    return render_template('index2.html')

@app.route("/blog/dog")
def blog2():
    return ("<p>I write about dogs </p>")