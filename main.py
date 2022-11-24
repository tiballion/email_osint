from tools.instagram import instagram
from tools.discord import discord
from tools.twitter import twitter
from tools.spotify import spotify


def main():
    email = input("Enter the email: ")
    print(instagram(email))
    print(discord(email))
    print(twitter(email))
    print(spotify(email))


if __name__ == "__main__":
    main()
