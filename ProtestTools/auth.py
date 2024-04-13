from propelauth_flask import current_user, init_auth
from flask import Flask
from app import app

auth = init_auth(
    auth_url="https://40436022.propelauthtest.com",
    api_key="ea60d75f6eb3c35433011d57e7b3dbc177cdbff2f0f11452215b4e39337789f1c10b1570c8e03eb0368ea651173620b9",
)


@app.route("/api/whoami")
@auth.require_user
def who_am_i():
    """This route is protected, current_user is always set"""
    return {"user_id": current_user.user_id}
