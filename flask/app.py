# import necessary libraries

import os
import io
import numpy as np
import tensorflow as tf

from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

# create route that renders index.html template
@app.route("/")

def home():
    return render_template("index.html")

# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":

        text = request.form["text"]

        return redirect("http://localhost:5000/", code=302)

    return render_template("home.html")


@app.route("/api/text")
def text():
    
    text_data = [{
        "text": text
            }]

    return jsonify(text_data)

if __name__ == "__main__":
    app.run()