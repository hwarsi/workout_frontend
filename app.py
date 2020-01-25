from flask import Flask, render_template, jsonify


workout_app = Flask(___name__)


@workout_app.route("/home")
def homePage():
    return render_template("index.html")

if __name__ == "___main___":
    workout_app.run()

