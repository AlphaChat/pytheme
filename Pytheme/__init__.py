from flask import Flask, request, session, abort
from .frontend import frontend

from .csrf_protect import generate_csrf_token


def create_app(config):

    app = Flask(__name__)

    app.config.from_object(__name__)
    app.config.from_object(f"Pytheme.config.{config}")

    app.jinja_env.globals["csrf_token"] = generate_csrf_token

    @app.before_request
    def csrf_protect():
        if request.method == "POST":
            token = session.pop("csrf_token", None)
            if not token or token != request.form.get("csrf_token"):
                abort(400)


    app.register_blueprint(frontend)

    return app
