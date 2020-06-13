#!/usr/bin/python3
from flask import jsonify


def ClientError(status_code=404, description='Not Found', error_message=''):
    return jsonify({'status_code': status_code, 'description': description, 'error': error_message})
