#!/usr/bin/python3
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity


@app_views.route('/user/<string:username>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def user(username):
    if request.method == 'GET':
        return "GET"
    elif request.method == "DELETE":
        return "DELETE"
    else:
        return "PUT"
    

@app_views.route('/users/<string:username>/topics', methods=["GET"])
@jwt_required()
def users(username):
    pass

@app_views.route('/users/<string:username>/topic/<string:topic_id>', methods=["GET", "POST", "DELETE"])
@jwt_required()
def user_topic(username, topic_id):
    pass

@app_views.route('/user/<string:username>/posts', methods=['GET'])
@jwt_required()
def user_posts(username):
    pass

@app_views.route('/user/<string:username>/post/<string:post_id>', methods=['POST', 'GET', 'PUT'])
@jwt_required()
def user_post(username, post_id):
    pass


@app_views.route('/user/<string:id>/reset', methods=['POST'])
def get_user(id):
    pass