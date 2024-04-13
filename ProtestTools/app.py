from flask import Flask, render_template
import logging
import folium
import configparser


app = Flask(__name__)
from auth import login
from map import create_pin
from event_view import view_events


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    app.config["MONGO_URI"] = config["MONGODB"]["URI"]
    app.run(debug=True)
