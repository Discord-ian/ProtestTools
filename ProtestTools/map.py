from flask import Flask, url_for, redirect, render_template, request
import folium
from app import app


@app.route("/map/create_pin", methods=["GET", "POST"])
def create_pin():
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
    if request.method == "GET":
        pass
    m = folium.Map(location=(38.9673769, -95.2793475))

    m.add_child(folium.ClickForMarker())

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template("createEvent.html", iframe=iframe)
