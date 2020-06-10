#!/usr/bin/python3
"""
Containing the Log class.
"""

from datetime import datetime
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.mysql import TEXT


class Log(BaseModel, Base):
    """The Log class."""
    __tablename__ = 'logs'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    #username = Column(String(255), ForeignKey('users.username'), nullable=False)
    session_start = Column(DateTime, nullable=False)
    session_end = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes log"""
        super().__init__(*args, **kwargs)
