#!/usr/bin/python3
"""
Containing the Comment class.
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, Unicode, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_imageattach.entity import Image, image_attachment
import uuid


class Comment(BaseModel, Base):
    """The Comment class."""
    __tablename__ = 'comments'
    text = Column(TEXT, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    post_id = Column(String(60), ForeignKey('posts.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes comment."""
        super().__init__(*args, **kwargs)
