from flask  import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h2>Hello, World</h2>"

@app.route("/test")
def hello():
    return "<h1>TEST</h>"    

@app.route("/test2")
def hello2():
    return "<h1>TEST2</h>"       

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)    