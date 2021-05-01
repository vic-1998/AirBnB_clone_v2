#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """display “Hello HBNB!!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_python(text='is cool'):
    """display “Python ”, followed by the value"""
    return 'C ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} id a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def t_number(n):
    """display a HTML page only if n is an integer:"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        des = 'even'
    else:
        des = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           des=des)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
