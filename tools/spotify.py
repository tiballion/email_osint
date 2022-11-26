import requests


def spotify(email):
    endpoint = "https://spclient.wg.spotify.com/signup/public/v1/account"
    data = {
        'validate': 1,
        'email': email
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    res = requests.post(endpoint, data=data, headers=headers)
    """if res.status_code == 200:
        if res.json()['status'] == 1:
            return 'Spotify \U0001f440'
        else:
            return 'Spotify [Not here!]'
    else:
        return 'Spotify [Couldn\'t check!]'"""
    return "Spotify checker not currently working"
