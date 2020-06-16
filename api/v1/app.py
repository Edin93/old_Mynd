#!/usr/bin/python3
""" Flask Application """
from flask import Flask, render_template, make_response, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
from security import authenticate, identity
from flask_jwt import JWT
from datetime import timedelta

UPLOAD_FOLDER = '/uploads/img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
jwt = JWT(app, authenticate, identity)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=60 * 60 * 24)
app.config["JWT_SECRET_KEY"] = "Mynd"
cors = CORS(app, resources={r"/*": {"origins": "*"}})



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
    app.run(host='0.0.0.0', port=5000, debug=True)
