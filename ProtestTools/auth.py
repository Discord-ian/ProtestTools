from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    current_app,
    Blueprint,
)


auth_func = Blueprint("auth_func", __name__)


@auth_func.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":


        print(request.form["username"] + " " + request.form["password"])
    error = None
    return render_template("login_page.html", error=error)
