#!/usr/bin/python3
"""
This is a Flask web application that listens on 0.0.0.0:5000 and
displays an HTML page similar to 8-index.html but with updated styles and data.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda x: x.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda x: x.name)
    places = storage.all(Place).values()
    reviews = storage.all(Review).values()
    return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places, reviews=reviews)

@app.teardown_appcontext
def teardown(exception):
    """Teardown method to remove the SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

