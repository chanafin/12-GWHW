from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape
#
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#

if __name__ == "__main__":
    app.run(debug=True)