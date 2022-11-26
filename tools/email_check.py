import re


def is_valid_email(email):
    return re.match(r"^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,3}$", email)
