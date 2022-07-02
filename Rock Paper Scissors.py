import random
from time import sleep


def play():
    print("Computer thinking.")
    sleep(1)
    print("Computer thinking..")
    sleep(1)
    print("Computer thinking...")
    sleep(1)
    hand = random.choice(['r', 'p', 's'])
    guess = input(
        "\nEnter your guess rock - 'r' , paper - 'p' , scissors - 's'\n: ")
    if guess == hand:
        print("\nYou WON!!!!\n")
    else:
        print(f"\nYou loseeee\nThe hand was {hand}")


while True:
    choice = input("To play enter 'play'\nTo exit enter 'exit'\n: ")
    if choice == "play":
        play()
    elif choice == "exit":
        exit()
    else:
        print("Invalid Entry")
