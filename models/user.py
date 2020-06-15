#!/usr/bin/python3
"""
Containing the User class.
"""

from datetime import datetime
import models
from models.base_model import BaseModel, Base
from models.post import Post
from models.comment import Comment
from models.topic import user_topic
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Enum, Date
from sqlalchemy.orm import relationship
import hashlib
from sqlalchemy_imageattach.entity import Image, image_attachment
# from flask_login import UserMixin


class User(BaseModel, Base):
    """The User class."""
    __tablename__ = 'users'
    username = Column(String(255), unique=True, nullable=False)
    fullname = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(155), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(Enum("Female", "Male"), nullable=False)
    last_login = Column(DateTime, default=datetime.utcnow, nullable=False)
    """profile_img = image_attachment('Post')
    """
    posts = relationship("Post", backref="user", cascade="all, delete, delete-orphan")
    comments = relationship("Comment", backref="user", cascade="all, delete, delete-orphan")
    logs = relationship("Log", backref="user", cascade="all, delete, delete-orphan")
    topics = relationship("Topic", secondary=user_topic, viewonly=False)
    likes = relationship("PostLike", backref="user", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        plain_text_pwd = None
        if kwargs:
            plain_text_pwd = kwargs.pop('password', None)
        if plain_text_pwd:
            User.hash_password(self, plain_text_pwd)
        super().__init__(*args, **kwargs)

    def hash_password(self, value):
        """Hash user password md5"""
        v = hashlib.md5(value.encode()).hexdigest()
        setattr(self, 'password', v)
