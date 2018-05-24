
class DefaultConfig(object):

    SECRET_KEY = None  # FIXME
    DEBUG = False
    TESTING = False

    SESSION_COOKIE_SECURE = True

    ATHEME_XMLRPC_ENDPOINT = "http://172.32.1.2:8080/xmlrpc"


class ProductionConfig(DefaultConfig):

    pass


class DevelopmentConfig(ProductionConfig):

    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False
