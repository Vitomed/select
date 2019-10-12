from flask import Flask


app = Flask(__name__)


@app.route("/login")
def login():
    return "<h1>Statr Flask</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=777)