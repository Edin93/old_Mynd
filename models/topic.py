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


post_topics = Table('post_topics', Base.metadata,
                    Column('post_id', String(255),
                           ForeignKey('posts.id', onupdate='CASCADE',
                               ondelete='CASCADE'),
                           primary_key=True),
                    Column('topic_id', String(255),
                           ForeignKey('topics.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True))

user_topics = Table('user_topics', Base.metadata,
                    Column('user_id', String(255),
                           ForeignKey('users.id', onupdate='CASCADE',
                               ondelete='CASCADE'),
                           primary_key=True),
                    Column('username', String(255),
                           ForeignKey('users.username', onupdate='CASCADE',
                               ondelete='CASCADE'),
                           primary_key=True),
                    Column('topic_id', String(255),
                           ForeignKey('topics.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True))

class Topic(BaseModel, Base):
    """The Topic class."""
    __tablename__ = 'topics'
    title = Column(String(255), nullable=False)
    description = Column(TEXT)
    posts = relationship("Post",
                         secondary=post_topics,
                         viewonly=False)
    users = relationship("User",
                         secondary=user_topics,
                         viewonly=False)

    def __init__(self, *args, **kwargs):
        """initializes topic"""
        super().__init__(*args, **kwargs)
