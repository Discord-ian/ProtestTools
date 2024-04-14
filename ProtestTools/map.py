from flask import render_template, request, Blueprint
import folium
from flask_login import login_required
from db import add_event, check_for_duplicate_event
from models import Event

map_functions = Blueprint("map", __name__)


@map_functions.route("/map/create_event", methods=["GET", "POST"])
@login_required
def create_event():
    # TODO: Add default country option somewhere in config
    # TODO: Timezone support
    """
    Form has fields:
    event_name
    event_date
    event_time
    event_address
    event_city
    event_zip
    event_state
    event_country
    :return:
    """
    error = None
    if request.method == "POST":
        event = Event()
        """
        Generate the massive event object to be stored in the MongoDB database.
        """
        event.name = request.form["event_name"]
        event.date = request.form["event_date"]
        event.time = request.form["event_time"]
        event.description = request.form["event_description"]
        event.cause = request.form["event_cause"]
        event.address = request.form["event_address"]
        event.city = request.form["event_city"]
        event.zip_code = request.form["event_zip"]
        event.state = request.form["event_state"]
        event.lat = request.form["lat"]
        event.lng = request.form["lng"]
        if not check_for_duplicate_event(key="event_name", value=event.name):
            error = "Duplicate Event Name"
            return render_template(
                "create_event.html", lat=38.9673769, long=-95.2793475, error=error
            )
        else:
            add_event(event)
    return render_template(
        "create_event.html", lat=38.9673769, long=-95.2793475, error=error
    )
