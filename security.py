from werkzeug.security import safe_str_cmp
from models.user import User
from models.log import Log
from models import storage
from flask  import jsonify
import hashlib
from datetime import datetime

def authenticate(username, password):
    user = storage.get_user_by_username(username)
    if user and safe_str_cmp(user.password.encode('utf-8'),  hashlib.md5(password.encode()).hexdigest()):
        log = Log()
        log.user_id = user.id
        log.session_start = datetime.utcnow()
        log.save()
        return user


def identity(payload):
    print(payload)
    user_id = payload['identity']
    return storage.get(User, user_id).to_dict()
