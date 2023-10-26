#!/usr/bin/python3
"""
This is a Flask web application that listens on 0.0.0.0:5000 and
has two routes:
- The root path ("/") displays "Hello HBNB!"
- The "/hbnb" path displays "HBNB"
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

