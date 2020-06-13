#!/usr/bin/python3
"""
Test models.
"""

from models.user import User
from models.post import Post
from models.comment import Comment
from models.post_like import PostLike
from models.log import Log
from models.topic import Topic
u1 = User()
u1.username = 'James'

u1.email = 'James@gmail.com'
u1.fullname = 'James Bond'
u1.password = 'jamespassword'
print('-------------- U1 -------------')
u1.save()
print(u1)
p1 = Post()
p1.path = 'this is path'
p1.user_id = u1.id
p1.description = 'this is description'
p1.save()
print(p1)
c1 = Comment()
c1.text = 'this is the first comment ever'
c1.user_id = u1.id
c1.post_id = p1.id
c1.save()
print(c1)
lk1 = PostLike()
lk1.post_id = p1.id
lk1.user_id = u1.id
lk1.save()
print(lk1)
lg = Log()
lg.user_id = u1.id
lg.save()
print(lg)
t1 = Topic()
t1.title = 'hotel'
t1.description = 'we love hotels'
t1.posts.append(p1)
t1.users.append(u1)
t1.save()
print(t1)
print("THIS IS U1.TOPICS!!")
print(u1.topics)
