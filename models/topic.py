#!/usr/bin/python3
"""
Containing the Topic class.
"""

from datetime import datetime
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TEXT


class Topic(BaseModel, Base):
    """The Topic class."""
    __tablename__ = 'topics'
    title = Column(String(255), nullable=False)
    description = Column(TEXT)

    def __init__(self, *args, **kwargs):
        """initializes topic"""
        super().__init__(*args, **kwargs)
