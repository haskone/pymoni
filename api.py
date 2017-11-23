from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json')
def data():
    return jsonify({"x": [234.3, 423.3, 44.5, 245.6, 987.5],
                    "y": ["1/10/2017 10:31", "1/10/2017 11:31",
                          "1/10/2017 12:31", "1/10/2017 13:31",
                          "1/10/2017 14:31"]})  

app.run()
