from tools.instagram import instagram


def main():
    email = input("Enter email: ")
    result = instagram(email)
    print(result)


if __name__ == "__main__":
    main()
