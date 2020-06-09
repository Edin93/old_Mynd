"""
Contains user authentication methods and routes redirections.
"""
from flask import Blueprint, render_template, redirect, url_for, request
from models.user import User


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.join'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, username=username, fullname=fullname, password=password)

    # add the new user to the database
    new_user.save()

    return redirect(url_for('auth.login'))
