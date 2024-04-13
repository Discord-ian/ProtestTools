from flask import Flask, render_template
from app import app


@app.route("/eventview")
def view_events():
    return render_template("event_viewer.html")
