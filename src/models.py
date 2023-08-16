import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String(20), nullable=False)
    birth_date = Column(String(20), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(20), nullable=False)

    posts = relationship("Post", backref="user")
    likes = relationship("Like", backref="user")
    comments = relationship("Comment", backref="user")

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(10), nullable=False)
    caption = Column(String(100), nullable=False)
    image_url = Column(Integer(200), nullable=False)
    created_by_user_id = Column(String(20), nullable=False)
    created_by_user_date = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    
    likes = relationship("Like", backref="post")
    comments = relationship("Comment", backref="post")

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    post_id = Column(Integer, ForeignKey("post.id"), nullable=True)
    comment_id = Column(Integer, ForeignKey("comment.id"), nullable=True)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    content = Column(String(100), nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)

    likes = relationship("Like", backref="comment")

render_er(Base, 'diagram.png')
