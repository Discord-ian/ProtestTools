from flask import render_template, request, Blueprint
import folium
from db import add_event
from models import Event

map_functions = Blueprint("map", __name__)


@map_functions.route("/map/create_pin", methods=["GET", "POST"])
def create_pin():
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
    if request.method == "POST":
        event = Event()
        event.name = request.form["event_name"]
        event.date = request.form["event_date"]
        event.time = request.form["event_time"]
        event.address = request.form["event_address"]
        event.city = request.form["event_city"]
        event.zip_code = request.form["event_zip"]
        event.state = request.form["event_state"]
        event.country = request.form["event_country"]
        add_event(event)
    iframe_map = folium.Map(location=(38.9673769, -95.2793475))

    iframe_map.add_child(folium.ClickForMarker())

    # set the iframe width and height
    iframe_map.get_root().width = "800px"
    iframe_map.get_root().height = "600px"
    iframe = iframe_map.get_root()._repr_html_()

    return render_template("createEvent.html", iframe=iframe)
