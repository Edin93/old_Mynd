#!/usr/bin/python3

from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity


@app_views.route('/post', methods=['POST'])
@jwt_required()
def post_comments():
    """Current user creates a new post."""
    pass

@app_views.route('/post/<string:post_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def post_comments(post_id):
    """Get, modify or delete a post."""
    pass


@app_views.route('/post/<string:post_id>/comments', methods=['POST', 'GET'])
@jwt_required()
def post_comments(post_id):
    """Get or post a post comments."""
    pass


@app_views.route('/post/<string:post_id>/comments/<string:comment_id>', methods=['DELETE', 'PUT'])
@jwt_required()
def post_comments(post_id, comment_id):
    """Modify or delete a post comment."""
    pass
