from .service import nickserv_command
from re import search


def info(account):
    data = nickserv_command("info", account)
    return NickservInfo(data=data)



def set_password(new_password):
    return nickserv_command("set", f"password {new_password}")


def set_email(new_email):
    return nickserv_command("set", f"email {new_email}")


def set_accountname(new_acct_name):
    return nickserv_command("set", f"accountname {new_acct_name}")

class NickservInfo:
  def __init__(self, data = None):
    if data is None:
      return
    self.parse_info(data)
    
  def parse_info(self, data):
    lines = data.split("\n")

    for line in lines:

      match = search("Registered\s+: (\w+ \d\d (?:\d\d|:)+ \d{4}) \+\d{4} (\((?:(?:\d+|\w)+\s)+ago\))", line)
      if match is not None:
        self.registered_on = match.group(1)
        self.registered_since = match.group(2)
        continue
      
      match = search("User reg\.\s+: (\w+ \d\d (?:\d\d|:)+ \d{4}) \+\d{4} (\((?:(?:\d+|\w)+\s)+ago\))", line)
      if match is not None:
       self.user_registered_on = match.group(1)
       self.user_registered_since = match.group(2)
       continue
      
      match = search("Entity ID\s+:\s((?:\w|\d)+)", line)
      if match is not None:
       self.entity_id = match.group(1)
       continue

      match = search("Last seen\s+: (\w+ \d\d (?:\d\d|:)+ \d{4}) \+\d{4} (\((?:(?:\d+|\w)+\s)+ago\))", line)
      if match is not None:
       self.last_seen = match.group(1)
       self.last_seen_since = match.group(2)
       continue

      match = search("Nicks\s+: (.*)", line)
      if match is not None:
       self.nicks = match.group(1)
       continue

      match = search("Email\s+: (.*@.*\.\w+)", line)
      if match is not None:
       self.email = match.group(1)
       continue
      
      match = search("Flags\s+: ((?:\w+|\,\s))+", line)
      if match is not None:
       self.flags = match.group(1)
       continue

      match = search("Channels\s+: ((?:\d \w+|\,\s))+", line)
      if match is not None:
       self.channels = match.group(1)
       continue

      match = search("Groups\s+: (\!(?:\w+|-|_)+|,\s)+", line)
      if match is not None:
       self.groups = match.groups(1)      
       continue

      

      


  