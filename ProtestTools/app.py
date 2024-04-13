from flask import Flask, render_template_string
import folium


app = Flask(__name__)


@app.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map()

    m.add_child(folium.ClickForMarker())

    folium.Marker((lat, lon), draggable=True).add_to(m)
    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    {{ iframe|safe }}
                </body>
            </html>
        """,
        iframe=iframe,
    )


if __name__ == "__main__":
    app.run(debug=True)
