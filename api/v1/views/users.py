#!/usr/bin/python3
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity


@app_views.route('/user/<string:user_id>', methods=['POST', 'GET', 'PUT'])
@jwt_required()
def user(user_id):
    # if request.method == 'POST':
    #     return 'POST'
    # elif request.method == 'GET':
    #     return "GET"
    # else:
    return user_id
    

@app_views.route('/users/')
@jwt_required()
def users():
    pass
