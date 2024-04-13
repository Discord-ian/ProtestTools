from flask import Flask, render_template
import logging
import folium


app = Flask(__name__)
from auth import login
from map import create_pin


if __name__ == "__main__":
    app.run(debug=True)
