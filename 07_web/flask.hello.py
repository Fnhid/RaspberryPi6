from flask import Flask

app = Flask(__name__)

# 0.0.0.0:5000
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/first">Go First</a>
        <a href="/second">Go Second</a>
    '''

@app.route("/first")
def first():
    return '''
        <p>This is first one..</p>
        <a href="/">Go main</a>
        <a href="/second">Go Second</a>
    '''

@app.route("/second")
def second():
    return '''
        <p>This is second one..</p>
        <a href="/">Go main</a>
        <a href="/first">Go First</a>
    '''    

if __name__ == "__main__":
    app.run(host="0.0.0.0")