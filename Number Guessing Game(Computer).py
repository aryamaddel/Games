import random


def play():
    random_number = random.randint(1, 10)
    guess = int(input("Enter your guess from one to ten: "))
    for i in range(2):
        if guess > random_number:
            guess = int(input("Guess Lower: "))
        elif guess < random_number:
            guess = int(input("Guess higher: "))
        elif guess == random_number:
            print("CORRECT!!")
        else:
            guess = int(input("Enter your guess from ONE to TEN: "))
        if i == 1:
            print("You loseeeee!")


while True:
    choice = input("To play enter 'play'\nTo exit enter 'exit'\n: ")
    if choice == "play":
        play()
    elif choice == "exit":
        exit()
    else:
        print("Invalid Entry")
