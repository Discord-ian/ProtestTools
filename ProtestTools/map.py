from flask import Flask, url_for, redirect, render_template, request
import folium
import logging
from app import app


@app.route("/map/create_pin", methods=["GET", "POST"])
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
        pass
    iframe_map = folium.Map(location=(38.9673769, -95.2793475))

    iframe_map.add_child(folium.ClickForMarker())

    # set the iframe width and height
    iframe_map.get_root().width = "800px"
    iframe_map.get_root().height = "600px"
    iframe = iframe_map.get_root()._repr_html_()

    return render_template("createEvent.html", iframe=iframe)
