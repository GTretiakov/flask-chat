import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    messages.append("{}:{}".format(username, message))

def get_all_messages():
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

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
