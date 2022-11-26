import requests


def get_csrf_token():
    crsf_token = requests.get("https://www.spotify.com/us/signup/").text.split('"csrf_token":"')[1].split('"')[0]
    return crsf_token


print(get_csrf_token())
