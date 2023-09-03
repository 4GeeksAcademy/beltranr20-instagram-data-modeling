import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import Table

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table post.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_name = Column(String(250))
    post_number = Column(String(250))
    post_id = Column(Integer, ForeignKey('user.id'))
    # comments: Mapped[List[Comments]] = relationship(secondary=association_table)

    def to_dict(self):
        return {}

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table comments.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comments_context = Column(String(250))
    comments_number = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

# class Base (declarative_base):
#     pass
# association_table = Table(
#     "association_table",
#     Base.metadata,
#     Column("post_id", ForeignKey("post.id")),
#     Column("comments", ForeignKey("comments.id")),
# )

class Followers (Base):
    __tablename__ = 'followers'
    # Here we define columns for the table comments.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    followers_username = Column(String(250))
    followers_number = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
