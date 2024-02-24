from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!!!"

@app.route("/hello1")
def hello_world1():
    return "Hello World 1!!!"

@app.route("/hello2")
def hello_world2():
    return "Hello World 2!!!"

@app.route("/test")
def test():
    a = 5 + 6
    return "this is my function {}".format(a)

@app.route('/request')
def request_input():
    # https://localhost:5000/request?x=kiran
    data = request.args.get('x')
    return "this is the input comes from url {}".format(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")