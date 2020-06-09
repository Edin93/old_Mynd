"""
Contains user authentication methods and routes redirections.
"""
from models import storage
from flask import Blueprint, render_template, redirect, url_for, request, Flask
from models.user import User

#auth = Blueprint('auth', __name__)
auth = Flask(__name__)

@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_submit():
    username = request.form.get('username')
    password = request.form.get('password')

@auth.route('/join', methods=['GET'])
def signup():
    return render_template('join.html')

@auth.route('/join', methods=['POST'])
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


if __name__ == "__main__":
    auth.run('0.0.0.0', 5000)
