#!/usr/bin/python3
"""
This is a Flask web application that listens on 0.0.0.0:5000 and
displays a list of states and their associated cities from the storage engine.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('9-states.html', states=states, state_id=None)

@app.route('/states/<state_id>', strict_slashes=False)
def states_by_id(state_id):
    state = storage.get(State, state_id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', states=[state], state_id=state_id, cities=cities)
    else:
        return render_template('9-states.html', states=None, state_id=None)

@app.teardown_appcontext
def teardown(exception):
    """Teardown method to remove the SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

