from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    current_app,
    Blueprint,
)
from app import client
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from models import User

auth_func = Blueprint("auth_func", __name__)


@auth_func.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try_login(request.form["username"], request.form["password"])
    error = None
    return render_template("login_page.html", error=error)


@auth_func.route("/create_user/<invite_id>", methods=["GET", "POST"])
def create_user(invite_id):
    if valid_new_user_link(invite_id):
        if request.method == "POST":
            # Decrement invite id uses
            generate_db_user(request.form["username"], request.form["password"])
            print(request.form["username"] + " " + request.form["password"])
        error = None
        return render_template("login_page.html", error=error)
    else:
        return redirect(url_for("eventview.view_events"))


def try_login(username, password):
    try:
        x = client.cx.ProtestTools.Users.find_one({"username": username})
        hashed_pw = generate_password_hash(password, method="pbkdf2", salt_length=16)
        if check_password_hash(password, x["password"]):
            user = User(username, hashed_pw)
            login_user(user, remember=True)
    except:
        return False


def generate_db_user(username, password, invite_id):
    hashed_pw = generate_password_hash(password, method="pbkdf2", salt_length=16)
    user = {"username": username, "password": hashed_pw}
    decrement_invite(invite_id)
    client.cx.ProtestTools.Users.insert_one(user)


def decrement_invite(invite_id):
    x = client.cx.ProtestTools.InviteLinks.find_one({"invite_id": invite_id})


def valid_new_user_link(inv_id):
    x = client.cx.ProtestTools.InviteLinks.find_one({"invite_id": inv_id})
    try:
        return x["invite_id"] == inv_id
    except TypeError:
        # Type error would occur if x ends up being None
        return False
