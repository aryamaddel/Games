from random import choice
from re import A

from Assets.words import words


def get_valid_word():
    word = choice(words)
    while ('-' or ' ') in word:
        word = choice(words)
    return word


def hangman(word):
    # # TEST!!!!!!!!!!!!!! LINE!!!!!!!!!!!!!!
    # print(word)
    # # TEST!!!!!!!!!!!!!! LINE!!!!!!!!!!!!!!

    print("\nGuess the word. Type one letter at a time.\n")
    print(f"The word is {len(word)} letters long\n")
    print("You have 6 chances\n")

    answer = ['_' for i in range(len(word))]
    print(*answer)
    for i in range(6):
        alphabet = input(": ")

        if alphabet in word:
            for index in range(len(word)):
                if word[index] == alphabet:
                    answer[index] = alphabet
            print(*answer)
            if answer == list(word):
                print("You Won")
                break

        else:
            if i < 4:
                print("\nAlphabet not present in word Try Again")

            else:
                print("\nAlphabet not present in word last chance")


hangman(get_valid_word())
