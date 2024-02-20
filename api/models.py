from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, UniqueConstraint, ForeignKey
from flask_migrate import Migrate

metadata = MetaData(naming_convention={
    'fk':'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
})

db = SQLAlchemy(metadata=metadata)

#************************Table Models********************************#
# User
# Tweet
# Like
# retweet
# share
# comment
# Follow


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(50), unique=True,nullable =  False)
    password = db.Column(db.String(50), nullable = False)

class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)

class like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)


class retweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Share(db.Model):
    __tablename__ = 'shares'

    id = db.Column(db.Integer, primary_key=True)

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)


class Follow(db.Model):
    __tablename__ = 'follows'


    id = db.Column(db.Integer, primary_key=True)
