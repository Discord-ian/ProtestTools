from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask import current_app, g
from app import client


def add_event(event_info):
    mongo = client.cx
    db = mongo.ProtestTools
    db.Events.insert_one(event_info.dict())


def find_user(username):
    """
    Searches DB for the specified username
    :param username:
    :return:
    """
