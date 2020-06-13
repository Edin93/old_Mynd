#!/usr/bin/python3
from models.user import User
from models.topic import Topic
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity
from api.v1.views.util.helpers import ClientError


@app_views.route('/user/<string:username>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def user(username):
    user = storage.get_user_by_username(username)
    is_me = current_identity['username'] == username
    if not user:
        return ClientError(404, 'User not found', 'Not Found')
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
            return ClientError(401, 'Access denied', 'Unauthorized')
        storage.delete(user)
        return {'status_code': 1, 'info': 'Deleted'}, 200
    else:
        if not is_me:
            return ClientError(401, 'Access denied', 'Unauthorized')
        can_update = ['gender', 'fullname', 'birth_date']
        for k, v in request.get_json().items():
            if k in can_update:
                setattr(user, k, v)
        user.save()
        return {"status_code": 1, "info": "Updated"}


@app_views.route('/users/<string:username>/topics', methods=["GET", "POST"])
@jwt_required()
def users(username):
    user = storage.get_user_by_username(username)
    is_me = current_identity['username'] == username
    if not user:
        return ClientError(404, 'User not found', 'Not Found')
    topics = user.topics
    if request.method == "GET":
        d = {"Topics": []}
        for t in topics:
            td = {"id": t.id, "title": t.title, "description": t.description}
            d["Topics"].append(td)
        return jsonify(d)
    else:
        if not is_me:
            return ClientError(401, 'Access denied', 'Unauthorized')
        topic = Topic()
        """
        here we're supposed to provide the user a fixed list of topics
        instead of creating a new one
        """
        if 'title' not in request.get_json():
            abort(400, description='No valid entry')
        desc = ''
        if 'description' in request.get_json():
            desc = request.get_json()['description']
        setattr(topic, 'title', request.get_json()['title'])
        setattr(topic, 'description', request.get_json()['desc'])
        topic.save()
        user.topics.append(topic)
        storage.save()
        return {"status_code": 1, "info": "Created"}



@app_views.route('/users/<string:username>/topic/<string:topic_id>', methods=["GET", "DELETE"])
@jwt_required()
def user_topic(username, topic_id):
    user = storage.get_user_by_username(username)
    is_me = current_identity['username'] == username
    if not user:
        return ClientError(404, 'User not found', 'Not Found')
    topics = user.topics
    for t in topics:
        if t.id == topic_id and request.method == "GET":
            td = {"id": t.id, "title": t.title, "description": t.description}
            return jsonify(td)
        elif t.id == topic_id and request.method == "DELETE":
            if not is_me:
                return ClientError(401, 'Access denied', 'Unauthorized')
            user.topics.remove(topic_id)
            storage.delete(t)
            storage.save()
            return {'status_code': 1, 'info': 'Deleted'}, 200


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
