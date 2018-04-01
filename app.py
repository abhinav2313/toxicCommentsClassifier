# import necessary libraries

import os
import io
import numpy as np
import tensorflow as tf

from flask import Flask, request, redirect, jsonify, render_template

from naive_bayes import nb

import keras
from keras import backend as K

train_url = 'train.csv'

nb_model = nb(train_url)

app = Flask(__name__)

model = None
graph = None

def load_model():
    global model
    global graph
    # add the model name 
    model = keras.models.load_model(nb_model)

    graph = K.get_session().graph

load_model()

# create route that renders index.html template
@app.route("/")

def home():
    return render_template("index.html")

# Query the database and send the jsonified results

@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        if 'sentence' not in request.form:
            print('No sentence post')
            redirect(request.url)
        elif request.form['sentence'] == '':
            print('No sentence')
            redirect(request.url)
        else:
            sent = request.form['sentence']
            sentiments = model.predict(sent)
        return render_template(sentence=sent)

    return render_template('home.html')

@app.route("/api/text")
def text():
    
    text_data = [{
        "text": text
            }]

    return jsonify(text_data)

if __name__ == "__main__":
    app.run()