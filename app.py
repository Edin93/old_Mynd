#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    return render_template('home.html', title='Home page')

@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html', title='About page')

@app.route('/login', strict_slashes=False)
def login():
    return render_template('login.html', title='Login')

@app.route('/join', strict_slashes=False)
def join():
    return render_template('join.html', title='Join')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
