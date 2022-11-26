import requests


def discord(email) -> str:
    endpoint = "https://discord.com/api/v9/auth/register"
    json_str = "{\"email\":\""+email+"\",\"username\":\"asdsadsad\",\"password\":\"q1e31e12r13*\",\"invite\":null,\"consent\":true,\"date_of_birth\":\"1973-05-09\",\"gift_code_sku_id\":null,\"captcha_key\":null,\"promotional_email_opt_in\":false}"

    r = requests.post(endpoint, data=json_str)
    if r.status_code == 400:
        if "EMAIL_ALREADY_REGISTERED" in r.text:
            return "Discord 🐀"
        else:
            return "Discord \U0001F6AB"
    elif r.status_code == 429:
        return "Discord [Rate limited!]"
    else:
        return "Discord [Couldn't check!], invalid status code"
