from flask import Flask, render_template
import logging
import folium
import configparser
from flask_pymongo import PyMongo


# Imports of routes
from map import map_functions
from auth import auth_func

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")
app.config["MONGO_URI"] = config["MONGODB"]["URI"]
app.register_blueprint(map_functions)
app.register_blueprint(auth_func)
