from payoffdata import payoffs

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return str(len(payoffs.keys()))

if __name__ == "__main__":
    app.run()
