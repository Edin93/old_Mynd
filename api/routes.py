#!/usr/bin/python3
from flask import Flask, render_template
from Mynd.api import app_views

@app_views.route('/', strict_slashes=False)
def base():
    return render_template('base.html', title='Mynd')

@app_views.route('/home', strict_slashes=False)
def home():
    return render_template('home.html', title='Home page')

@app_views.route('/about', strict_slashes=False)
def about():
    return render_template('about.html', title='About page')

