from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)

from . import atheme
from .atheme import nickserv

frontend = Blueprint("frontend", __name__)


@frontend.route("/")
def index():

    if "accountname" not in session or "authcookie" not in session:
        flash("You must login first.", "warning")
        return redirect(url_for("frontend.login"))

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
def service_nickserv():

    info = nickserv.info("cruzr")

    return render_template("nickserv.html", info=info)
