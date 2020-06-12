#!/usr/bin/python3
"""
Contains user authentication methods and routes redirections.
"""
from api.v1.views import app_views
from datetime import datetime
from flask import abort, Blueprint, render_template, redirect, url_for, request, Flask, session
from models.user import User
from models.log import Log
from models import storage
from flask_jwt import JWT, jwt_required, current_identity
from datetime import  datetime


@app_views.route('/join', methods=['POST'])
def signup_submit():
    if not request.get_json():
        abort(400, description='Not a JSON')
    entry_form = ['email', 'fullname', 'username',
                  'password', 'birth_date', 'gender']
    for i in entry_form:
        if i not in request.get_json():
            abort(400, description='No valid entry')
    if storage.unique_user(request.get_json()['email'], request.get_json()['username']) is False:
        return {'status_code': 0, 'info': 'Already exist'}
    user = User(**request.get_json())
    user.save()
    return {"status_code": 1}


@app_views.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    user_id  = current_identity['id']
    log = storage.get_log_by_user_id(user_id)
    if log:
        log.session_end = datetime.utcnow()
        log.save()
    else:
        return {'status_code': 0, 'redirect': '/login'}
    return {'status_code': 1, 'info': 'User successfully logout'}
