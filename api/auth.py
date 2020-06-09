#!/usr/bin/python3
"""
Contains user authentication methods and routes redirections.
"""
from Mynd.api import app_views
from flask import Blueprint, render_template, redirect, url_for, request, Flask
from Mynd.models.user import User


@app_views.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app_views.route('/profile', methods=['GET'])
def get_user_profile():
    return render_template('profile.html')

@app_views.route('/login', methods=['POST'])
def login_submit():
    username = request.form.get('username')
    password = request.form.get('password')

    if storage.correct_user_credentials(username, password):
        return redirect('/profile')
    return redirect('/login')

@app_views.route('/join', methods=['GET'])
def signup():
    return render_template('join.html')

@app_views.route('/join', methods=['POST'])
def signup_submit():
    email = request.form.get('email')
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')

    if storage.unique_user(email, username) is False:
        return redirect('/join')

    new_user = User(email=email, username=username, fullname=fullname, password=password)
    new_user.save()
    return redirect('/login')
