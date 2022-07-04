import string
from random import choice

from Assets.words import words


def get_valid_word():
    word = choice(words)
    while (" " or "-") in word:
        word = choice(words)
    return word.upper()


def hangman(word):
    print(word)
    lives = 6
    word_letters = set(word)

    alphabet = set(string.ascii_uppercase)

    used_letters = set()

    while len(word_letters) > 0 and lives>0:
        print("You have used:", " ".join(used_letters), '\n')
        word_list = [
            letter if letter in used_letters else "_" for letter in word]
        print('Current word: ', ' '.join(word_list))

        # Getting user input
        user_letter = input("\nEnter : ").upper()
        print("")

        # IF entered letter is available to guess or been already guessed or wrong character
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            # IF entered letter is present in the CORRECT word 
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("Letter not present in the word Try again")
                lives -= 1
                print(f"\nYou have {lives} left\n")

        # Letter repetion
        elif user_letter in used_letters:
            print("\nYou already guessed that word Try again\n")
        else:
            print("\nYou typed something wrong type again\n")
    
    if lives == 0:
        print("\nYou Died\n")
        print(f"\nThe Word was {word}\n")
    else:
        print("\nYou won\n")
        print(f"\nThe Word was {word}\n")


hangman(get_valid_word())
