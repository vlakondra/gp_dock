from flask  import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h2>Hello, World!!</h2>"

@app.route("/test")
def hello():
    return "<h1>TEST</h>"    