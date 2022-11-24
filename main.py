from tools.instagram import instagram
from tools.discord import discord


def main():
    email = input("Enter email: ")
    print(instagram(email))
    print(discord(email))


if __name__ == "__main__":
    main()
