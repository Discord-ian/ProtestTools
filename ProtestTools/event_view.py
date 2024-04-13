from flask import Flask, render_template, Blueprint
import folium

# page contains list of created events and displays event information on click
eventview = Blueprint("eventview", __name__)


@eventview.route("/eventview")
def view_events():
    # TODO: add information to main from database on click
    # TODO: add links to individual event pages
    # set the iframe width and height
    iframe_map = folium.Map(location=(38.9673769, -95.2793475))
    iframe_map.get_root().width = "800px"
    iframe_map.get_root().height = "600px"
    iframe = iframe_map.get_root()._repr_html_()

    return render_template("event_viewer.html", iframe=iframe)


@eventview.route("/eventpage")
def event_info():

    # set the iframe width and height
    iframe_map = folium.Map(location=(38.9673769, -95.2793475))
    iframe_map.get_root().width = "800px"
    iframe_map.get_root().height = "600px"
    iframe = iframe_map.get_root()._repr_html_()

    return render_template("default_event.html", iframe=iframe)
