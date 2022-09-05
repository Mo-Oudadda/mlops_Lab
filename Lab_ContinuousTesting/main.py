import re


def is_email(text):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", text))


def is_username(name):
    if name.isalnum():
        return True
    return False


def is_password(password):
    if len(password) < 8 or not any(p.isdigit() for p in password):
        return False
    else:
        return True
