from tools.instagram import instagram
from tools.discord import discord
from tools.twitter import twitter
from tools.spotify import spotify
from tools.email import is_valid_email


def main():
    email = input("Enter the email: ")
    if is_valid_email(email):
        res = [instagram(email), discord(email), twitter(email), spotify(email)]
        for r in res:
            print(r)
    else:
        print("Invalid email!")
        exit()


if __name__ == "__main__":
    main()
