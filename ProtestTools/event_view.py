from flask import Flask, render_template, Blueprint, redirect, url_for
from db import get_event_dicts, valid_event_id, get_event_info
from flask_login import current_user
import folium

# page contains list of created events and displays event information on click
eventview = Blueprint("eventview", __name__)


@eventview.route("/")
def view_events():
    # TODO: add information to main from database on click
    # TODO: add links to individual event pages
    # set the iframe width and height
    iframe_map = folium.Map(location=(38.9673769, -95.2793475))
    iframe = iframe_map.get_root()._repr_html_()
    events = get_event_dicts()
    return render_template(
        "event_viewer.html", iframe=iframe, events=events, user=current_user
    )


@eventview.route("/event/<event_id>")
def event_info(event_id):
    if valid_event_id(event_id):
        iframe_map = folium.Map(location=(38.9673769, -95.2793475))
        iframe = iframe_map.get_root()._repr_html_()
        event = get_event_info(event_id)
        return render_template("default_event.html", iframe=iframe, event=event)
    else:
        return redirect(url_for("eventview.view_events"))
    # set the iframe width and height
