import requests


def get_csrf_token():
    session = requests.Session()
    res = session.get("http://open.spotify.com/token")
    return res.json().get("t")


def aa():
    api_request = requests.Session()
    csrf_token = get_csrf_token()
    email = "test@gmail.com"
    password = "test123"

    cookies = {"fb_continue": "https%3A%2F%2Fwww.spotify.com%2Fid%2Faccount%2Foverview%2F",
               "sp_landing": "play.spotify.com%2F", "sp_landingref": "https%3A%2F%2Fwww.google.com%2F",
               "user_eligible": "0", "spot": "%7B%22t%22%3A1498061345%2C%22m%22%3A%22id%22%2C%22p%22%3Anull%7D",
               "sp_t": "ac1439ee6195be76711e73dc0f79f89", "sp_new": "1", "csrf_token": csrf_token,
               "__bon": "MHwwfC0zMjQyMjQ0ODl8LTEzNjE3NDI4NTM4fDF8MXwxfDE=", "remember": "false@false.com",
               "_ga": "GA1.2.153026989.1498061376", "_gid": "GA1.2.740264023.1498061376"}
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4",
        "Accept": "application/json, text/plain", "Content-Type": "application/x-www-form-urlencoded"}
    payload = {"remember": "false", "username": email, "password": password, "csrf_token": csrf_token}

    response = api_request.post("https://accounts.spotify.com/api/login", data=payload, headers=headers,
                                cookies=cookies)
    print(response.text)

# ezPf1IfFfqEaLitLvOp4SziDs9QFdHwU
aa()