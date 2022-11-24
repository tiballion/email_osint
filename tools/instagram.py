import requests
import re


def get_token():
    url_string = "https://www.instagram.com/accounts/emailsignup/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
    }
    r = requests.get(url_string, headers=headers)
    if r.status_code == 200:
        token = re.search(r'(?m){\\"config\\":{\\"csrf_token\\":\\"(.*?)\\"', r.text).group(1)
    else:
        token = "-1"
    return token


def instagram(email):
    try:
        token = get_token()
        if token == "":
            res = "Instagram [Couldn't check!]"
        else:
            endpoint = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
            data = {"email": email}
            r = requests.post(endpoint, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                                 "Cookie": "csrftoken="+token+";",
                                                 "X-Csrftoken": token}, data=data)
            if r.status_code == 200:
                if "email_is_taken" in r.text:
                    res = "Instagram \U0001f440"
                else:
                    res = "Instagram [Not here!]"
            else:
                res = "Instagram [Couldn't check!]"
    except Exception as e:
        print(e)
        res = "Instagram [Couldn't check!]"
    return res
