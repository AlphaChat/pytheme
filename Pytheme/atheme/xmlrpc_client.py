from xmlrpc.client import ServerProxy

def create_xmlrpc_client(app):
    with app.app_context():
        return ServerProxy(app.config["ATHEME_XMLRPC_ENDPOINT"])
