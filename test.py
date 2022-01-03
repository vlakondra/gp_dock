from flask  import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    a=7/0
    return "<h2>Hello, World</h2>"

@app.route("/test")
def hello():
    return "<h1>TEST</h>"    

@app.route("/test2")
def hello2():
    return "<h1>TEST2</h>"       