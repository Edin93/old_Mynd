#!/usr/bin/python3
"""
Containing the Post class.
"""

import models
from models.base_model import BaseModel, Base
from models.topic import post_topic
from sqlalchemy import Column, ForeignKey, Integer, Unicode, String
from sqlalchemy.dialects.mysql import TEXT
"""from sqlalchemy_imageattach.entity import Image
"""
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    """The Post class."""
    __tablename__ = 'posts'
    path = Column(String(255), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    description = Column(TEXT, nullable=True)
    comments = relationship("Comment", backref="posts",
                            cascade="all, delete, delete-orphan")
    likes = relationship("PostLike", backref="posts",
                            cascade="all, delete, delete-orphan")
    topics = relationship("Topic",
                         secondary=post_topic,
                         viewonly=False)
    def __init__(self, *args, **kwargs):
        """Initializes post."""
        super().__init__(*args, **kwargs)
