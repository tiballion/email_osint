import requests
import json


def twitter(email):
    endpoint = "https://api.twitter.com/i/users/email_available.json"
    data = {"email": email}
    r = requests.get(endpoint, params=data, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    if r.status_code == 200:
        body = json.loads(r.content)
        if body["taken"]:
            res = "Twitter \U0001f440"
        else:
            res = "Twitter [Not here!]"
    else:
        res = "Twitter [Couldn't check!]"
    return res
