#!/usr/bin/python3
"""
Containing the PostLike class.
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid


class PostLike(BaseModel, Base):
    """The PostLike class."""
    __tablename__ = 'post_likes'
    post_id = Column(String(255), nullable=False, ForeignKey('posts.id'))
    username = Column(String(255), nullable=False, ForeignKey('users.username'))

    def __init__(*args, **kwargs):
        """Initializes post."""
        super().__init__(*args, **kwargs)
