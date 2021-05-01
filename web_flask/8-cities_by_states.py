#!/usr/bin/python3
"""a"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """a"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_app(exception):
    """Call in this method storage.close()"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
