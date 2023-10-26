#!/usr/bin/python3
"""
This is a Flask web application that listens on 0.0.0.0:5000 and
has four routes:
- The root path ("/") displays "Hello HBNB!"
- The "/hbnb" path displays "HBNB"
- The "/c/<text>" path displays "C ", followed by the value of the text variable
  (replace underscore _ symbols with a space)
- The "/python/<text>" path displays "Python ", followed by the value of the text variable
  (replace underscore _ symbols with a space). The default value for text is "is cool."
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return "C " + text

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return "Python " + text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

