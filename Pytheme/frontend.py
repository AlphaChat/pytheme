from functools import wraps

from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)

from . import atheme
from .atheme import nickserv

frontend = Blueprint("frontend", __name__)


def login_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if "accountname" not in session or "authcookie" not in session:
            flash("You must login to view this page", "info")
            return redirect(url_for("frontend.login"))

        return function(*args, **kwargs)

    return wrapper


@frontend.route("/")
@login_required
def index():
    return render_template("index.html")


@frontend.route("/login", methods=["GET", "POST"])
def login():

    if "accountname" in session and "authcookie" in session:
        flash("You are alerady logged in.", "warning")
        return redirect(url_for("frontend.index"))

    accountname = request.form.get("accountname")
    password = request.form.get("password")

    # *logs password* lol i work at twitter

    if request.method == "POST":
        if not accountname and not password:
            flash("Username and password required", "error")
            return redirect(url_for("frontend.login"))

        authcookie = atheme.login(accountname, password)

        if authcookie is None:
            return redirect(url_for("frontend.login"))

        session["accountname"] = accountname
        session["authcookie"] = authcookie

        return redirect(url_for("frontend.index"))

    return render_template("login.html")


@frontend.route("/logout")
def logout():
    session.pop("accountname", None)
    session.pop("authcookie", None)

    flash("You have successfully logged out.")  # even if you never logged in

    return redirect(url_for("frontend.login"))


@frontend.route("/nickserv")
@login_required
def service_nickserv():

    info = nickserv.info(session["accountname"])

    return render_template("nickserv.html", info=info)
