from flask import Flask , render_template

app = Flask(__name__)


@app.route("/")

def home():
    return render_template("index.html")


# @app.route("/signup")

# def signup():
#     return render_template("signup.html")


app.run(debug = True)