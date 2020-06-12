#!/usr/bin/python3
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity


@app_views.route('/user/<string:username>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def user(username):
    user = storage.get_user_by_username(username)
    if not user:
        abort(404, description='User not found')
    is_me = current_identity['username'] == username
    if request.method == 'GET':
        user = user.to_dict()
        to_hide = ['birth_date', 'created_at', 'email',
                   'gender', 'last_login', 'updated_at']
        del user['password']
        if current_identity['username'] != username:
            for i in to_hide:
                del user[i]
        return jsonify(user)
    elif request.method == "DELETE":
        if not is_me:
            abort(401, description='Unauthorized')
        storage.delete(user)
        return {'status_code': 1, 'info': 'Deleted'}, 200
    else:
        return "PUT"


@app_views.route('/users/<string:username>/topics', methods=["GET"])
@jwt_required()
def users(username):
    pass


@app_views.route('/users/<string:username>/topic/<string:topic_id>', methods=["POST", "DELETE"])
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
