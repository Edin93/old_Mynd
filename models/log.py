#!/usr/bin/python3
"""
Containing the Log class.
"""

from datetime import datetime
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TEXT


class Log(BaseModel, Base):
    """The Log class."""
    __tablename__ = 'logs'
    username = Column(String(255), ForeignKey('users.username'), nullable=False)
    user_id = Column(String(255), foreignKey('users.user_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes log"""
        super().__init__(*args, **kwargs)
