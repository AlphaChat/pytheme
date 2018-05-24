from .service import nickserv_command


def info(account):
    return nickserv_command("info", account)
