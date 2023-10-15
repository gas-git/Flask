from flask import Flask

import json

app = Flask(__name__)


@app.route('/')
def hello():

    for i in range(1, 5000):
        with open('stress.json') as stress_file:
            data = json.load(stress_file)
        return data


    