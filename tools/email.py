import re


def is_valid_email(email):
    if re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
        return True
    else:
        return False
