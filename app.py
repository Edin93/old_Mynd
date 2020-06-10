#!/usr/bin/python3
""" Flask Application """
from flask import Flask, render_template, make_response, jsonify
from models import storage
from models.user import User
from api import app_views
from flask_cors import CORS
from flask_login import LoginManager
from api.auth import *

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/Mynd/*": {"origins": "*"}})

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
# since the user_id is just the primary key of our user table, use it in the query for the user
    return storage.get(User, user_id)


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=5000)
