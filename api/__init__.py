#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/')

from Mynd.api.auth import *
from Mynd.api.routes import *
