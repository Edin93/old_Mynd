#!/usr/bin/python3
""" Flask Application """
from flask import Flask, render_template, make_response, jsonify
from models import storage
from models.user import User
from api import app_views
from flask_cors import CORS
from api.auth import *
from werkzeug.security import safe_str_cmp
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity


UPLOAD_FOLDER = '/uploads/img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
jwt = JWT(app, authenticate, identity)
app.config["JWT_SECRET_KEY"] = "Mynd"
cors = CORS(app, resources={r"/Mynd/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.route('/protected')
@jwt_required()
def protected():
    return current_identity


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=5000)
