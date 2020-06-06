#!/usr/bin/python3
"""
Test models.
"""

from models.engine.db_storage import DBStorage
from models.user import User
dbs = DBStorage()
u1 = User()
u1.username = 'James'
u1.email = 'James@gmail.com'
u1.password = 'jamespassword'
print('-------------- U1 -------------')
print(u1)
dbs.new(u1)
dbs.save()
