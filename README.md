# Pytheme

Flask frontend to Atheme's XMLRPC interface.

## Setup

1. Copy `config.example.py` to `config.py`, and set the `SECRET_KEY` and `ATHEME_XMLRPC_ENDPOINT` settings appropriately.
2. Using the Python `virtualenv` module, create a virtual environment in the project directory. (install with `pip install virtualenv`)
    1. `$ virtualenv venv` (UNIX)
    2. `> virtualenv venv` (Windows)
3. Activate virtual environment
    1. `$ source venv/bin/activate` (UNIX)
    2. `> .\venv\Scripts\activate` (Windows)
4. Install project requirements
    1. `pip install -U -r requirements.txt`
5. Set the following environment variables
    1. `FLASK_APP=app.py`
    2. `FLASK_DEBUG=1` (only if running in devel mode obviously)
    3. `PYTHEME_CONFIG=ProductionConfig` (only if running in prod obviously)
6. Start Flask: `flask run`


## Warnings ⚠️
- Please do NOT run Atheme's XMLRPC on a public interface. Use SSH tunneling, a VPN, or run Pytheme on the same machine as Atheme and connect them via localhost.
- Please do NOT have Pytheme run on HTTP/S ports. Put it behind NGiNX and possibly uWSGI when running in production.
