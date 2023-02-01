from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", number=10)


@app.route("/search")
def search():
    return "Search Page"

# dinamik url oluşturma


@app.route("/search/<string:id>")
def searchId(id):
    return "Id:" + id


if __name__ == "__main__":
    app.run(debug=True)
