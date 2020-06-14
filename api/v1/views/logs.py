#!/usr/bin/python3

from models.log import Log
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity
from api.v1.views.util.helpers import ClientError


@app_views.route('/logs', methods=['GET'])
@jwt_required()
def logs():
    """Get all logs."""
    logs = storage.all(Log).values()
    logs = [log.to_dict() for log in logs]
    return jsonify({'status_code': 1, 'record': 'logs', 'logs': logs})


@app_views.route('/logs/activity', methods=['GET'])
@jwt_required()
def activity_logs():
    """Get all username logs."""
    logs = storage.all(Log).values()
    logs = [log.to_dict() for log in logs if log.to_dict()['user_id'] == current_identity['id']]
    return jsonify({'status_code': 1, 'user_id': current_identity['id'], 'logs': logs})
