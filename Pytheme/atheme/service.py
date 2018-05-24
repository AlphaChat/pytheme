
from xmlrpc.client import Fault

from flask import current_app, flash, request, session

from .xmlrpc_client import create_xmlrpc_client


def service_command(service, command, params):
    """ run a command on an atheme service """
    client = create_xmlrpc_client(current_app)

    account = session["accountname"]
    authcookie = session["authcookie"]
    ip = request.remote_addr

    result = None

    try:
        result = client.atheme.command(authcookie, account, ip,
                                       service, command, params)
    except Fault as error:
        flash(f"Command Error {error.faultCode}: {error.faultString}")

    return result


def nickserv_command(command, params):
    return service_command("nickserv", command, params)


def chanserv_command(command, params):
    return service_command("chanserv", command, params)


def memoserv_command(command, params):
    return service_command("memoserv", command, params)


def operserv_command(command, params):
    return service_command("operserv", command, params)
