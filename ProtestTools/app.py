from flask import Flask, render_template
import logging
import folium
import configparser
from flask_pymongo import PyMongo
from flask_login import login_manager

client = PyMongo()

# Imports of routes
from map import map_functions
from auth import auth_func
from event_view import eventview

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")
app.config["MONGO_URI"] = config["MONGODB"]["URI"]
app.config["SECRET_KEY"] = config["FLASK"]["SECRET_KEY"]
app.register_blueprint(map_functions)
app.register_blueprint(auth_func)
app.register_blueprint(eventview)
client.init_app(app)
