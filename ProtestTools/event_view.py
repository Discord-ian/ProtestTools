from flask import Flask, render_template
import folium
from app import app


@app.route("/eventview")
def view_events():
    # set the iframe width and height
    iframe_map = folium.Map(location=(38.9673769, -95.2793475))
    iframe_map.get_root().width = "800px"
    iframe_map.get_root().height = "600px"
    iframe = iframe_map.get_root()._repr_html_()

    return render_template("event_viewer.html", iframe=iframe)
