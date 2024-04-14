from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask import current_app, g

from app import client
from models import User, Event
from bson import ObjectId


def add_event(event_info):
    mongo = client.cx
    db = mongo.ProtestTools
    db.Events.insert_one(event_info.dict())


def find_user(user_Id):
    """
    Searches DB for the specified username
    :param username:
    :return:
    """
    mongo = client.cx
    db = mongo.ProtestTools
    try:
        user = db.Users.find_one({"_id": ObjectId(user_Id)})
        return User(username=user["username"], id=["_id"])
    except TypeError:
        return None


def get_event_dicts():
    mongo = client.cx
    db = mongo.ProtestTools
    events = db.Events.find()
    return_list = []
    for event in events:
        return_list.append(event)
    return return_list


def valid_event_id(event_id):
    mongo = client.cx
    db = mongo.ProtestTools
    try:
        event = db.Events.find_one({"_id": ObjectId(event_id)})
        if event is not None:
            return True
        else:
            return False
    except TypeError:
        return False


def get_event_info(event_id):
    mongo = client.cx
    db = mongo.ProtestTools
    try:
        event = db.Events.find_one({"_id": ObjectId(event_id)})
        return event
    except TypeError:
        return None


def check_for_duplicate_user(key, value):
    x = client.cx.ProtestTools.Users
    duplicate = x.find_one({key: value})
    if duplicate is not None:
        return False
    else:
        return True


def check_for_duplicate_event(key, value):
    x = client.cx.ProtestTools.Events
    duplicate = x.find_one({key: value})
    if duplicate is not None:
        return False
    else:
        return True
