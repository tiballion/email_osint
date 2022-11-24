from tools.instagram import instagram
from tools.discord import discord
from tools.twitter import twitter


def main():
    email = input("Enter the email: ")
    print(instagram(email))
    print(discord(email))
    print(twitter(email))


if __name__ == "__main__":
    main()
