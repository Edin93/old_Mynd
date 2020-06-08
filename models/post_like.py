#!/usr/bin/python3
"""
Containing the PostLike class.
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, Unicode, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid


class PostLike(BaseModel, Base):
    """The PostLike class."""
    __tablename__ = 'post_likes'
    post_id = Column(String(60), ForeignKey('posts.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes post."""
        super().__init__(*args, **kwargs)
