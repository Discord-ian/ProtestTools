from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    current_app,
    Blueprint,
)
from bson import ObjectId
from flask_login import current_user, login_required
from app import client
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_urlsafe
from flask_login import login_user
from models import User

auth_func = Blueprint("auth_func", __name__)


@auth_func.route("/login", methods=["GET", "POST"])
def login():
    # TODO: Add redirect to event creation page
    if current_user.is_authenticated:
        return redirect(url_for("eventview.view_events"))
    if request.method == "POST":
        if try_login(request.form["username"], request.form["password"]):
            return redirect(request.args.get("next") or "eventview.view_events")
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
            if decrement_invite(invite_id):
                generate_db_user(
                    request.form["username"], request.form["password"], invite_id
                )
        return render_template("signup_page.html", error=error)
    else:
        return redirect(url_for("eventview.view_events"))


@auth_func.route("/generate_invite", methods=["GET", "POST"])
@login_required
def generate_invite():
    # Flask endpoint to generate an invite
    invite_url = None
    if request.method == "POST":
        print(request.form)
        invite_url = create_invite(request.form["invite_uses"])
        print(invite_url)
    return render_template("generate_invite.html", invite_url=invite_url)


def try_login(username, password):
    """
    Attempts to login a user by first looking up the relevant username in the databse
    :param username:
    :param password:
    :return:
    """
    try:
        x = client.cx.ProtestTools.Users.find_one({"username": username})
        if check_password_hash(x["password"], password):
            print("hi)")
            user = User(username, id=x["_id"])
            print("trying to log in")
            login_user(user, remember=True)
            return True
    except ValueError as e:
        print(e)
        return False


def generate_db_user(username, password, invite_id):
    hashed_pw = generate_password_hash(password, method="pbkdf2", salt_length=16)
    user = {"username": username, "password": hashed_pw}
    client.cx.ProtestTools.Users.insert_one(user)


def decrement_invite(invite_id):
    try:
        x = client.cx.ProtestTools.InviteLinks.find_one({"invite_id": invite_id})
        data_id = x["_id"]
        x["uses"] = int(x["uses"]) - 1
        if int(x["uses"]) > 0:
            client.cx.ProtestTools.InviteLinks.replace_one(
                {"_id": data_id}, x, upsert=True
            )
        else:
            client.cx.ProtestTools.InviteLinks.delete_one({"_id": data_id})
        return True
    except ValueError:
        # There might have been another user using the invite
        return False


def valid_new_user_link(inv_id):
    x = client.cx.ProtestTools.InviteLinks.find_one({"invite_id": inv_id})
    try:
        return x["invite_id"] == inv_id
    except TypeError:
        # Type error would occur if x ends up being None
        return False


def create_invite(uses):
    """
    Generates an invite with a given amount of uses. Saves the ID to MongoDB
    :param uses:
    :return:
    """
    invite_id = token_urlsafe(16)
    invite = {"invite_id": invite_id, "uses": int(uses)}
    client.cx.ProtestTools.InviteLinks.insert_one(invite)
    return url_for("auth_func.create_user", invite_id=invite_id, _external=True)
