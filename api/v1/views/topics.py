#!/usr/bin/python3

from models.topic import Topic
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity


@app_views.route('/topics', methods=['GET'])
def get_topics():
    pass


@app_views.route('/topic/<string:topic_id>', methods=['GET', 'PUT'])
def get_topic_posts(topic_id):
    pass

@app_views.route('/topic', methods=['POST'])
@jwt_required()
def new_topic():
    if current_identity['is_admin']:
        pass
