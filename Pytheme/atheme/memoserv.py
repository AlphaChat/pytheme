import re

from .service import memoserv_command

MEMO_LIST = re.compile(r"\- ([0-9]+) From: ([^ ]+) Sent: (.+)")


def list_memos(new_only=False):
    """ Returns a list of memos separated by ID, Sender, and Date """
    memos = []

    resp = memoserv_command("list")

    if resp is None:
        return

    for memo in MEMO_LIST.finditer(resp):
        if new_only and "[unread]" not in memo.group(3):
            continue

        memos.append((memo.group(1), memo.group(2), memo.group(3)))

    return memos


def read(memo_id):
    return memoserv_command("read", memo_id)


def send(account, message):
    return memoserv_command("send", f"{account} {message}")


def delete(memo_id):
    return memoserv_command("delete", memo_id)
