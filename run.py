import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_messages(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}:{}".format(now, username, message))

def get_all_messages():
    return "<br>".join(messages)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])
    return render_template("index.html")


@app.route('/<username>')
def user(username):
    return "<h1>welcome, {}</h1>{}".format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    add_messages(username, message)
    return redirect("/" + username)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
