import os

from Pytheme import create_app

app = create_app(os.environ.get("PYTHEME_CONFIG", "DevelopmentConfig"))


if __name__ == "__main__":
    app.run()
