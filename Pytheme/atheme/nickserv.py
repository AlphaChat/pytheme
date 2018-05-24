from .service import nickserv_command


def info(account):
    return nickserv_command("info", account)


def set_password(new_password):
    return nickserv_command("set", f"password {new_password}")


def set_email(new_email):
    return nickserv_command("set", f"email {new_email}")


def set_accountname(new_acct_name):
    return nickserv_command("set", f"accountname {new_acct_name}")
