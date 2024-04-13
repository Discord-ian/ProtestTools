from flask import Flask, redirect, render_template, request, url_for
from app import app


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form["username"] + " " + request.form["password"])
    error = None
    return render_template("login_page.html", error=error)
