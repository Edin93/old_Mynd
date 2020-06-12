#!/usr/bin/python3

from models.log import Log
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity

@app_views.route('/logs', methods=['GET'])
@jwt_required()
def post_comments():
    """Get all logs."""
    pass


@app_views.route('/logs/<string:username>', methods=['GET'])
@jwt_required()
def post_comments(username):
    """Get all username logs."""
    pass
