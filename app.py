from flask import Flask, render_template, request, redirect  # Import redirect
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hc!nhxXFgfia9R",
    database="mywebapp"
)


@app.route("/")
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return render_template("index.html", users=users)


@app.route("/add_user", methods=["POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s)", (username, email)
        )
        db.commit()
        cursor.close()

    return redirect("/")  # Use redirect function to redirect to the index route


if __name__ == "__main__":
    app.run(debug=True)
