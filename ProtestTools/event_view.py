from flask import Flask, render_template, Blueprint, redirect, url_for
from db import get_event_dicts, valid_event_id, get_event_info
from datetime import datetime
from flask_login import current_user, login_required
import folium

# page contains list of created events and displays event information on click
eventview = Blueprint("eventview", __name__)


@eventview.route("/")
@login_required
def view_events():
    """
    Route to main page which shows the map with all current event markers.
    Has list on the side to give more info about each event
    :return:
    """
    events = get_event_dicts()
    iframe_map = folium.Map(location=(38.9673769, -95.2793475))
    for event in events:
        d = datetime.strptime(event["time"], "%H:%M")
        event["twelve_hr"] = d.strftime("%I:%M %p")
        folium.Marker(
            location=(event["location"]["lat"], event["location"]["lng"]),
            popup=event["event_name"],
        ).add_to(iframe_map)
    iframe = iframe_map.get_root()._repr_html_()
    return render_template(
        "event_viewer.html", iframe=iframe, events=events, user=current_user
    )


@eventview.route("/event/<event_id>")
@login_required
def event_info(event_id):
    if valid_event_id(event_id):
        twelve_hr = None
        event = get_event_info(event_id)
        d = datetime.strptime(event["time"], "%H:%M")
        twelve_hr = d.strftime("%I:%M %p")
        location = event["location"]
        address = (
            location["address"]
            + "\r\n"
            + location["city"]
            + ", "
            + location["state"]
            + " "
            + location["zip_code"]
        )
        iframe_map = folium.Map(
            location=(location["lat"], location["lng"]), zoom_start=13
        )
        event = get_event_info(event_id)
        folium.Marker(
            location=(float(location["lat"]), float(location["lng"])), popup=address
        ).add_to(iframe_map)
        iframe = iframe_map.get_root()._repr_html_()
        return render_template(
            "default_event.html", iframe=iframe, event=event, twelve_hour=twelve_hr
        )
    else:
        return redirect(url_for("eventview.view_events"))
    # set the iframe width and height
