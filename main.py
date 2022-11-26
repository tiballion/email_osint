from tools.instagram import instagram
from tools.discord import discord
from tools.twitter import twitter
from tools.spotify import spotify
from tools.email import is_valid_email


def header():
    """Prints the header"""
    print("""
888       888 888                                                                                   .d8888b.  
888   o   888 888                                                                                  d88P  Y88b 
888  d8b  888 888                                                                                       .d88P 
888 d888b 888 88888b.   .d88b.        8888b.  888d888 .d88b.       888  888  .d88b.  888  888         .d88P"  
888d88888b888 888 "88b d88""88b          "88b 888P"  d8P  Y8b      888  888 d88""88b 888  888         888"    
88888P Y88888 888  888 888  888      .d888888 888    88888888      888  888 888  888 888  888         888     
8888P   Y8888 888  888 Y88..88P      888  888 888    Y8b.          Y88b 888 Y88..88P Y88b 888                 
888P     Y888 888  888  "Y88P"       "Y888888 888     "Y8888        "Y88888  "Y88P"   "Y88888         888     
                                                                        888                                   
                                                                   Y8b d88P                                   
                                                                    "Y88P"                                    
    """)


def main():
    # header()
    # email = input("Enter the email: ")
    # if is_valid_email(email):
        # res = [instagram(email), discord(email), twitter(email), spotify(email)]
        # for r in res:
            # print(r)
    # else:
        # print("Invalid email!")
        # exit()
    print(spotify("test@fdp.com"))


if __name__ == "__main__":
    main()
