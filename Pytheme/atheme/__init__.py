
from xmlrpc.client import Fault

from flask import (current_app, flash, make_response, redirect, request,
                   session, url_for)

from .xmlrpc_client import create_xmlrpc_client



def login(accountname, password):
    client = create_xmlrpc_client(current_app)

    authcookie = None

    try:
        authcookie = client.atheme.login(accountname, password,
                                         request.remote_addr)
    except Fault as error:
        if error.faultCode == 1:
            abort(500)  # invalid parameters
        elif error.faultCode == 3 or error.faultCode == 5:
            flash("Invaild accountname or password.", "error")
        elif error.faultCode == 6:
            flash("Your services account has been frozen.", "error")

    return authcookie


def logout():
    accountname = request.cookies.get("accountname")
    authcookie = request.cookies.get("authcookie")

    if accountname is None or authcookie is None:
        flash("You're not logged in.", "error")
        return redirect(url_for("app.login"))

    client = create_xmlrpc_client(current_app)
    client.atheme.logout(accountname, authcookie)

