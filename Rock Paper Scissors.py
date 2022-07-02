import random
from time import sleep


def play():
    print("Computer thinking.")
    sleep(1)
    print("Computer thinking..")
    sleep(1)
    print("Computer thinking...")
    computer_hand = random.choice(['r', 'p', 's'])
    user_hand = input(
        "\nEnter your guess rock - 'r' , paper - 'p' , scissors - 's'\n: ")
    if user_hand == computer_hand:
        print("\nIt's a TIE\n")

    elif user_hand == 'r':
        if computer_hand == 'p':
            print(f"You lost the computer's hand was {computer_hand}\n")
        elif computer_hand == 's':
            print(f"You Won the computer's hand was {computer_hand}\n")

    elif user_hand == 'p':
        if computer_hand == 's':
            print(f"You lost the computer's hand was {computer_hand}\n")
        elif computer_hand == 'r':
            print(f"You Won the computer's hand was {computer_hand}\n")

    elif user_hand == 's':
        if computer_hand == 'r':
            print(f"You lost the computer's hand was {computer_hand}\n")
        elif computer_hand == 'p':
            print(f"You Won the computer's hand was {computer_hand}\n")


while True:
    choice = input("To play enter 'play'\nTo exit enter 'exit'\n: ")
    if choice == "play":
        play()
    elif choice == "exit":
        exit()
    else:
        print("Invalid Entry")
