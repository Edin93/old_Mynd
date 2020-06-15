#!/usr/bin/python3
"""
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.users import *
from api.v1.views.auth import *
from api.v1.views.logs import *
from api.v1.views.posts import *
from api.v1.views.topics import *
from api.v1.views.likes import *
