#!/usr/bin/python3
"""
Containing the Topic class.
"""

from datetime import datetime
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import relationship


post_topic = Table('post_topic', Base.metadata,
                    Column('post_id', String(60),
                           ForeignKey('posts.id', onupdate='CASCADE',
                               ondelete='CASCADE')),
                    Column('topic_id', String(60),
                           ForeignKey('topics.id', onupdate='CASCADE',
                                      ondelete='CASCADE')))

user_topic = Table('user_topic', Base.metadata,
                    Column('user_id', String(60),
                           ForeignKey('users.id', onupdate='CASCADE',
                               ondelete='CASCADE')),
                    Column('topic_id', String(60),
                           ForeignKey('topics.id', onupdate='CASCADE',
                                      ondelete='CASCADE')))

class Topic(BaseModel, Base):
    """The Topic class."""
    __tablename__ = 'topics'
    title = Column(String(255), nullable=False)
    description = Column(TEXT)
    posts = relationship("Post",
                         secondary=post_topic,
                         viewonly=False)
    users = relationship("User",
                         secondary=user_topic,
                         viewonly=False)

    def __init__(self, *args, **kwargs):
        """initializes topic"""
        super().__init__(*args, **kwargs)
