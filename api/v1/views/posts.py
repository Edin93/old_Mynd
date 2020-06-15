#!/usr/bin/python3

from models.comment import Comment
from models.topic import Topic
from models.user import User
from models.post import Post
from models.post_like import PostLike
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity
from api.v1.views.util.helpers import ClientError


@app_views.route('/user/<string:username>/posts', methods=['GET', 'POST'])
@jwt_required()
def user_posts(username):
    """Gets user posts, Current user creates a new post."""

    user = storage.get_user_by_username(username)
    is_me = current_identity['username'] == username
    if not user:
        return ClientError(404, 'User not found', 'Not Found')
    if request.method == 'GET':
        posts = user.posts
        d = {"Posts": []}
        for p in posts:
            post_topics = [topic.title for topic in p.topics]
            dp = {"id": p.id, "path": p.path, "description": p.description,
                  "topics": post_topics, "likes": len(p.likes),
                  "comments": len(p.comments)}
            d["Posts"].append(dp)
        return jsonify(d)
    elif request.method == 'POST':
        if not is_me:
            return ClientError(401, 'Access denied', 'Unauthorized')
        if not request.get_json():
            return ClientError(400, 'Not a JSON', 'Invalid')
        if 'path' not in request.get_json():
            return ClientError(400, 'No valid Entry', 'Invalid')
        post = Post()
        post.path = request.get_json()['path']
        if 'description' in request.get_json():
            post.description = request.get_json()['description']
        if 'topic_ids' in request.get_json():
            for topic_id in request.get_json()['topic_ids']:
                topic = storage.get(Topic, topic_id)
                if topic:
                    post.topics.append(topic)
        if 'topic_titles' in request.get_json():
            for title in request.get_json()['topic_titles']:
                topic = storage.get_topic_by_title(title)
                if topic:
                    post.topics.append(topic)
        post.user_id = user.id
        post.save()
        return {"status_code": 1, "info": "Created"}


@app_views.route('/user/<string:username>/post/<string:post_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def user_post(username, post_id):
    """Get, modify or delete a post."""

    user = storage.get_user_by_username(username)
    is_me = current_identity['username'] == username
    if not user:
        return ClientError(404, 'User not found', 'Not Found')
    post = storage.get(Post, post_id)
    if not post:
        return ClientError(404, 'Post not found', 'Not Found')
    if post not in user.posts:
        return ClientError(404, 'Post not found for this user', 'Not Found')
    if request.method == 'GET':
        post_topics = [topic.title for topic in post.topics]
        return jsonify({"id": post.id, "path": post.path,
                                "description": post.description,
                                "topics": post_topics,
                                "likes": len(post.likes),
                                "comments": len(post.comments)})
    if not is_me:
        return ClientError(401, 'Access denied', 'Unauthorized')
    if request.method == 'DELETE':
        storage.delete(post)
        storage.save()
        return {'status_code': 1, 'info': 'Deleted'}, 200
    elif not request.get_json():
        return ClientError(400, 'Not a JSON', 'Invalid')
    if 'path' in request.get_json():
        setattr(post, 'path', request.get_json()['path'])
    if 'description' in request.get_json():
        setattr(post, 'description', request.get_json()['description'])
    if 'topic_ids' in request.get_json():
        post.topics = []
        for topic_id in request.get_json()['topic_ids']:
            topic = storage.get(Topic, topic_id)
            if topic:
                post.topics.append(topic)
    if 'topic_titles' in request.get_json():
        post.topics = []
        for title in request.get_json()['topic_titles']:
            topic = storage.get_topic_by_title(title)
            if topic:
                post.topics.append(topic)
    storage.save()
    return {"status_code": 1, "info": "Updated"}


@app_views.route('/user/<string:username>/post/<string:post_id>/topics', methods=['GET', 'POST'])
@jwt_required()
def post_topics(username, post_id):
    """ get topics of a post, add one topic to a post """
    user = storage.get_user_by_username(username)
    is_me = current_identity['username'] == username
    if not user:
        return ClientError(404, 'User not found', 'Not Found')
    post = storage.get(Post, post_id)
    if not post:
        return ClientError(404, 'Post not found', 'Not Found')
    if post not in user.posts:
        return ClientError(404, 'Post not found for this user', 'Not Found')
    if request.method == 'GET':
        topic_list = [topic.title for topic in post.topics]
        return jsonify(topic_list)
    if not is_me:
        return ClientError(401, 'Access denied', 'Unauthorized')
    if 'topic_id' in request.get_json():
        topic = storage.get(Topic, request.get_json()['topic_id'])
    elif 'topic_title' in request.get_json():
        topic = storage.get_topic_by_title(request.get_json()['topic_title'])
    if not topic:
        return ClientError(404, 'Topic not found', 'Not Found')
    post.topics.append(topic)
    storage.save()
    return {"status_code": 1, "info": "Topic added"}


@app_views.route('/user/<string:username>/post/<string:post_id>/topic/<string:topic_id>', methods=['GET', 'DELETE'])
@jwt_required()
def post_topic(username, post_id, topic_id):
    """ check if a topic is related to a post, delete the topic from post topics """
    user = storage.get_user_by_username(username)
    is_me = current_identity['username'] == username
    if not user:
        return ClientError(404, 'User not found', 'Not Found')
    post = storage.get(Post, post_id)
    if not post:
        return ClientError(404, 'Post not found', 'Not Found')
    if post not in user.posts:
        return ClientError(404, 'Post not found for this user', 'Not Found')
    topic = storage.get(Topic, topic_id)
    if not topic:
        return ClientError(404, 'Topic not found', 'Not Found')
    if topic not in post.topics:
        return ClientError(404, 'Topic not found for this post', 'Not Found')
    if request.method == 'GET':
        return {"status_code": 1, "info": "Post contains this topic"}
    if not is_me:
        return ClientError(401, 'Access denied', 'Unauthorized')
    post.topics.remove(topic)
    storage.save()
    return {"status_code": 1, "info": "Topic deleted from this post"}


@app_views.route('/post/<string:post_id>/comments', methods=['POST', 'GET'])
@jwt_required()
def post_comments(post_id):
    """Get the comments of a post, or adds a comment"""
    post = storage.get(Post, post_id)
    if not post:
        return ClientError(404, 'Post not found', 'Not Found')
    user = storage.get(User, post.user_id)
    if request.method == 'GET':
        d = {'Post owner': user.username, 'Post id': post_id, 'number of comments': len(post.comments), 'comments': []}
        for comment in post.comments:
            dc = {'comment id': comment.id,
                  'written by': storage.get(User, comment.user_id).username,
                  'content': comment.text}
            d['comments'].append(dc)
        return jsonify(d)
    if not request.get_json():
        return ClientError(400, 'Not a JSON', 'Invalid')
    comment = Comment()
    comment.user_id = current_identity['id']
    comment.post_id = post_id
    if 'text' in request.get_json() and request.get_json()['text'].strip() != "":
        comment.text = request.get_json()['text']
    elif 'content' in request.get_json() and request.get_json()['content'].strip() != "":
        comment.text = request.get_json()['content']
    else:
        return ClientError(400, 'Empty comments are not allowed', 'Error')
    comment.save()
    return {"status_code": 1, "info": "Created"}


@app_views.route('/post/<string:post_id>/comment/<string:comment_id>', methods=['DELETE', 'PUT'])
@jwt_required()
def edit_post_comment(post_id, comment_id):
    """Modify or delete a post comment."""
    post = storage.get(Post, post_id)
    if not post:
        return ClientError(404, 'Post not found', 'Not Found')
    comment = storage.get(Comment, comment_id)
    if not comment or comment not in post.comments:
        return ClientError(404, 'Comment Not Found', 'Not Found')
    user = storage.get(User, post.user_id)
    if comment.user_id != current_identity['id'] and current_identity['id'] != user.id:
        return ClientError(401, 'Access denied', 'Unauthorized')
    if request.method == 'DELETE':
        storage.delete(comment)
        storage.save()
        return {"status_code": 1, "info": "Comment Deleted"}
    if comment.user_id != current_identity['id']:
        return ClientError(401, 'Access denied', 'Unauthorized')
    if not request.get_json():
        return ClientError(400, 'Not a JSON', 'Invalid')
    if 'text' in request.get_json() and request.get_json()['text'].strip() != "":
        comment.text = request.get_json()['text']
    elif 'content' in request.get_json() and request.get_json()['content'].strip() != "":
        comment.text = request.get_json()['content']
    else:
        return ClientError(400, 'Empty comments are not allowed', 'Error')
    storage.save()
    return {"status_code": 1, "info": "Updated"}


@app_views.route('/post/<string:post_id>/like', methods=['POST'])
@jwt_required()
def like_post(post_id):
    """ likes a post """
    post = storage.get(Post, post_id)
    if not post:
        return ClientError(404, 'Post not found', 'Not Found')
    for like in post.likes:
        if like.user_id == current_identity['id']:
            return {"status_code": 1, "info": "You already like it!"}
    new_like = PostLike()
    new_like.user_id = current_identity['id']
    new_like.post_id = post_id
    new_like.save()
    return {"status_code": 1, "info": "Post successfully liked"}


@app_views.route('/post/<string:post_id>/unlike', methods=['POST'])
@jwt_required()
def unlike_post(post_id):
    """ unlike a post """
    post = storage.get(Post, post_id)
    if not post:
        return ClientError(404, 'Post not found', 'Not Found')
    for like in post.likes:
        if like.user_id == current_identity['id']:
            storage.delete(like)
            storage.save()
            return {"status_code": 1, "info": "Post successfully unliked"}
    return {"status_code": 1, "info": "You already don't like it"}


@app_views.route('/post/<string:post_id>/likes/', methods=['GET'])
@jwt_required()
def post_likers(post_id):
    """ returns likers of a post"""
    post = storage.get(Post, post_id)
    if not post:
        return ClientError(404, 'Post not found', 'Not Found')
    d = {'post id': post.id, 'number of likes': len(post.likes), 'liked by': []}
    for like in post.likes:
        d['liked by'].append(storage.get(User, like.user_id).username)
    return jsonify(d)
