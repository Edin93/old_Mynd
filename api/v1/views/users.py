#!/usr/bin/python3
from models.user import User
from models.topic import Topic
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity
from api.v1.views.util.helpers import ClientError


@app_views.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = storage.all(User).values()
    return jsonify({"count": len(users), "users": [{"id": user.id, "username": user.username} for user in users]})

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
        storage.save()
        return {'status_code': 1, 'info': 'Deleted'}
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
        d = { 'user_id': user.id, 'username': user.username, "Topics": []}
        for t in topics:
            td = {"id": t.id, "title": t.title, "description": t.description}
            d["Topics"].append(td)
        return jsonify(d)
    else:
        if not is_me:
            return ClientError(401, 'Access denied', 'Unauthorized')
        if 'id' in request.get_json():
            topic = storage.get(Topic, request.get_json()['id'])
            if not topic:
                return ClientError(404, 'Topic not found', 'Not Found')
            if topic in user.topics:
                return ClientError(409, "Topic already followed")
            user.topics.append(topic)
            storage.save()
            return {"status_code": 1, "info": "Topic added"}
        if 'title' in request.get_json():
            all_topics = storage.all(Topic).values()
            for topic in all_topics:
                if topic.title == request.get_json()['title']:
                    if topic in user.topics:
                        return ClientError(409, "Topic already followed")
                    user.topics.append(topic)
                    storage.save()
                    return {"status_code": 1, "info": "Topic added"}
            return ClientError(404, 'Topic not found', 'Not Found')


@app_views.route('/users/<string:username>/topic/<string:topic_id>', methods=["GET", "DELETE"])
@jwt_required()
def user_topic(username, topic_id):
    user = storage.get_user_by_username(username)
    is_me = current_identity['username'] == username
    if not user:
        return ClientError(404, 'User not found', 'Not Found')
    topic = storage.get(Topic, topic_id)
    if not topic:
        return ClientError(404, 'Topic not found', 'Not Found')

    if topic not in user.topics:
        return ClientError(404, 'Topic not found for this user', 'Not Found')

    if request.method == "GET":
        user_posts = [post for post in user.posts if topic in post.topics]
        return jsonify({
            'record': 'User posts with a specific topic',
            'topic_id': topic.id,
            'topic_title': topic.title,
            'username': user.username,
            'user_id': user.id,
            'posts': user_posts
        })
    elif request.method == "DELETE":
        if not is_me:
            return ClientError(401, 'Access denied', 'Unauthorized')
        user.topics.remove(topic)
        storage.save()
        return {'status_code': 1, 'info': 'Deleted'}


@app_views.route('/user/<string:id>/reset', methods=['POST'])
def get_user(id):
    pass
