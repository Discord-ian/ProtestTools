from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask import current_app, g


def connect_db():
    pymongo = PyMongo(current_app)
    return pymongo


def add_event(event_info):
    client = connect_db().cx
    db = client.ProtestTools
    db.Events.insert_one(event_info.json())
