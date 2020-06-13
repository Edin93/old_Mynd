#!/usr/bin/python3

from models.topic import Topic
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity
from api.v1.views.util.helpers import ClientError


@app_views.route('/topics', methods=['GET'])
@jwt_required()
def get_topics():
    topics = storage.all(Topic).values()
    topics = [topic.to_dict() for topic in topics]
    return jsonify({'records': 'topics', 'topics': topics, 'count': len(topics)})


@app_views.route('/topic/<string:topic_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def get_topic_posts(topic_id):
    topic = storage.get(Topic, topic_id)
    if not topic:
        return ClientError(404, 'Topic not found')
    if request.method == 'GET':
        return jsonify(topic.to_dict())
    elif request.method == 'PUT':
        ignore = ['id', 'update_at', 'created_at']
        data = request.get_json()
        for key, value in data.items():
            if key not in ignore:
                setattr(topic, key, value)
        storage.save()
        return jsonify({'status_code': 1, 'topic': topic.to_dict()})
    else:
        storage.delete(topic)
        storage.save()
        return jsonify({'status_code': 1, 'info': 'Deleted'})


@app_views.route('/topic', methods=['POST'])
@jwt_required()
def new_topic():
    if request.method == 'POST':
        title = request.get_json()['title']
        description = request.get_json()['description']
        if title is None:
            return ClientError(301, 'Invalid entry')
        topic = Topic(**{'title': title, 'description': description})
        topic.save()
        return jsonify({'status_code': 1, 'id': topic.id})
