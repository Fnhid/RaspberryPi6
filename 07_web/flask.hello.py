from flask import Flask

app = Flask(__name__)

# 0.0.0.0:5000
@app.route("/")
def hello():
    return "<p>Hello, Flask!!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")