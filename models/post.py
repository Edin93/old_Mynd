#!/usr/bin/python3
"""
Containing the Post class.
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_imageattach.entity import Image, image_attachment
import uuid


class Post(BaseModel, Base, Image):
    """The Post class."""
    __tablename__ = 'posts'
    path = Column(String(255), nullable=False)
    username = Column(String(255), ForeignKey('users.username'))
    user_id = Column(String(255), ForeignKey('users.id'))
    description = Column(TEXT, nullable=True)

    def __init__(*args, **kwargs):
        """Initializes post."""
        super().__init__(*args, **kwargs)
