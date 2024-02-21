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
    tweets = db.relationship('Tweet', back_populates='user', lazy=True)
    likes = db.relationship('Like', back_populates='user')
    retweets = db.relationship('Retweet', back_populates='retweeter')
    shares = db.relationship('Share', back_populates='sharer')
    comments = db.relationship('Comment', back_populates='commenter')
    followers = db.relationship('Follow', foreign_keys='Follow.followed_id', back_populates='followed', lazy='dynamic')
    following = db.relationship('Follow', foreign_keys='Follow.follower_id', back_populates='follower', lazy='dynamic')

    

class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False )
    user = db.relationship('User', back_populates='tweets', lazy=True)
    likes = db.relationship('Like', back_populates='tweet', lazy=True)
    retweets = db.relationship('Retweet', back_populates='original_tweet', lazy=True)
    shares = db.relationship('Share', back_populates='original_tweet', lazy=True)
    comments = db.relationship('Comment', back_populates='tweet', lazy=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())



class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'))
    user = db.relationship('User', back_populates='likes')
    tweet_id = db.relationship('Tweet', back_populates='likes')


class Retweet(db.Model):
    __tablename__ = 'retweets'


    id = db.Column(db.Integer, primary_key=True)
    original_tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'), nullable=False)
    retweeter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    original_tweet = db.relationship('Tweet', back_populates='retweets')
    retweeter = db.relationship('User', back_populates='retweets')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())




class Share(db.Model):
    __tablename__ = 'shares'

    id = db.Column(db.Integer, primary_key=True)
    original_tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'), nullable=False)
    sharer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    original_tweet = db.relationship('Tweet', back_populates='shares')
    sharer = db.relationship('User', back_populates='shares')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'), nullable=False)
    commenter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tweet = db.relationship('Tweet', back_populates='comments')
    commenter = db.relationship('User', back_populates='comments')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())



class Follow(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    follower = db.relationship('User', foreign_keys=[follower_id], back_populates='following')
    followed = db.relationship('User', foreign_keys=[followed_id], back_populates='followers')
