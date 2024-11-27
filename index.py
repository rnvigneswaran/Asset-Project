from flask import *

import mysql.connector

connection = mysql.connector.connect(
             host = "127.0.0.1",
             user = "root",
             password = "PassworD@0409",
             database = "gatepass_project"                
                                     
)

cursor = connection.cursor()

conquery = """CREATE TABLE IF NOT EXISTS userlog (username VARCHAR(250), password INTEGER);"""

cursor.execute(conquery)




app = Flask(__name__)


@app.route("/")

def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)