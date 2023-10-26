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

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    cities = {}
    for state in states:
        cities[state] = sorted([city for city in state.cities], key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states, cities=cities)

@app.teardown_appcontext
def teardown(exception):
    """Teardown method to remove the SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

