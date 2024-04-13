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
from secrets import token_urlsafe
from flask_login import login_user
from models import User

auth_func = Blueprint("auth_func", __name__)


@auth_func.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try_login(request.form["username"], request.form["password"])
    error = None
    return render_template("login_page.html", error=error)


@auth_func.route("/signup/<invite_id>", methods=["GET", "POST"])
def create_user(invite_id):
    if valid_new_user_link(invite_id):
        error = None
        if request.method == "POST":
            if request.form["password"] != request.form["password2"]:
                error = "Passwords do not match."
                return render_template("signup_page.html", error=error)
            # TODO: Decrement invite id uses
            generate_db_user(
                request.form["username"], request.form["password"], invite_id
            )
        return render_template("signup_page.html", error=error)
    else:
        return redirect(url_for("eventview.view_events"))


@auth_func.route("/generate_invite", methods=["GET", "POST"])
def generate_invite():
    invite_url = None
    if request.method == "POST":
        print(request.form)
        invite_url = create_invite(request.form["invite_uses"])
        print(invite_url)
    return render_template("generate_invite.html", invite_url=invite_url)


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


def create_invite(uses):
    invite_id = token_urlsafe(16)
    invite = {"invite_id": invite_id, "uses": uses}
    client.cx.ProtestTools.InviteLinks.insert_one(invite)

    return url_for("auth_func.create_user", invite_id=invite_id, _external=True)
