#!/usr/bin/python3
"""
Contains user authentication methods and routes redirections.
"""
from api import app_views
from datetime import datetime
from flask import abort, Blueprint, render_template, redirect, url_for, request, Flask, session
from models.user import User
from models import storage
from flask_login import login_user, logout_user, login_required


@app_views.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app_views.route('/users/<string:username>', methods=['GET'])
def user_profile(username):
    user = storage.get_user_by_username(username)
    if user:
        return render_template('profile.html', title=username, user=user)
    abort(404)


@app_views.route('/login', methods=['POST'])
def login_submit():
    username = request.form.get('username')
    password = request.form.get('password')
    u = storage.correct_user_credentials(username, password)
    if u:
        # session['logged_in'] = True
        u.last_login = datetime.utcnow()
        u.save()
        login_user(u)

    #     return redirect('/profile/' + u.username)
    # return redirect('/login')


@app_views.route('/logout')
@login_required
def logout():
    session['logged_in'] = False
    logout_user()
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
    birth_date = request.form.get('birth_date')
    gender = request.form.get('gender')
    if storage.unique_user(email, username) is False:
        return redirect('/join')
    new_user = User(gender=gender, birth_date=birth_date, email=email,
                    username=username, fullname=fullname, password=password)
    new_user.save()
    return redirect('/login')
