#!/usr/bin/python3
"""
Containing the class DBStorage.
"""

import models
from models.base_model import Base
from models.user import User
from models.comment import Comment
from models.topic import Topic
from models.log import Log
from models.post_like import PostLike
from models.post import Post
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import hashlib


classes = {"User": User, "Post": Post, "Comment": Comment, "PostLike": PostLike, "Log": Log, "Topic": Topic}

class DBStorage:
    """DBStorage class."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = "mynd_user"
        HBNB_MYSQL_PWD = "mynd"
        HBNB_MYSQL_HOST = "localhost"
        HBNB_MYSQL_DB = "mynd"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def unique_user(self, email, username):
        """
        query on the current database session
        and checks if the user already exists or not yet
        """
        users = self.__session.query(User).all()
        for u in users:
            if u.username == username or u.email == email:
                return False
        return True

    def correct_user_credentials(self, username, password):
        """
        query on the current database session
        and checks if the user already exists or not yet
        """
        p = hashlib.md5(password.encode()).hexdigest()
        users = self.__session.query(User).all()
        for u in users:
            if u.username == username and u.password == p:
                return True
        return False
