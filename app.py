from flask import Flask

import json

import time



app = Flask(__name__)


@app.route('/')
def hello():

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    for i in range(1, 50):
        with open('stress.json') as stress_file:
            
            data = json.load(stress_file)
            stress_file.close()

            for item in data['testing']:
                item['Time'] = item['Time'] = current_time


            with open('stress.json', "w") as stress_file:
                json.dump(data, stress_file)
                stress_file.close()

        
        return {"testing": [{"Name": "Glen Gardiner", "Expertise": "Stressing", "Country_of_birth": "Ireland", "Time": current_time}]}


if __name__ == "__main__":
    app.run(host="0.0.0.0")