#!/usr/bin/python3

from models.comment import Comment
from models import storage
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity
