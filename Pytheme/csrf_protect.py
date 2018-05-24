import os
import secrets
from flask import current_app, session


def generate_csrf_token():
    """
    Generate a CSRF token, stick it in the session, and return it for use in
    the template.

    NOTE: We don't have to bother validating it because anything set on
    the session is cryptographically signed anyway, so as long as the token
    in the POST request session and matches what's in the form, we're good.
    """
    key = current_app.config["SECRET_KEY"]
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_urlsafe(64)
    return session["csrf_token"]


