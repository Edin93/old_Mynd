#!/usr/bin/python3
"""
Containing the Post class.
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, Unicode, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy_imageattach.entity import Image
from sqlalchemy.orm import relationship


class Post(BaseModel, Base, Image):
    """The Post class."""
    __tablename__ = 'posts'
    path = Column(String(255), nullable=False)
    username = Column(String(255), ForeignKey('users.username'), nullable=False)
    user_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    description = Column(TEXT, nullable=True)
    comments = relationship("Comment", backref="posts",
                            cascade="all, delete, delete-orphan")
    likes = relationship("PostLike", backref="posts",
                            cascade="all, delete, delete-orphan")

    def __init__(*args, **kwargs):
        """Initializes post."""
        super().__init__(*args, **kwargs)
