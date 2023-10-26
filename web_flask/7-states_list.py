#!/usr/bin/python3
"""
This is a Flask web application that listens on 0.0.0.0:5000 and
displays a list of states from the storage engine.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(exception):
    """Teardown method to remove SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

