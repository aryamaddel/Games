from random import randint


def guess(x):
    lower = 1
    upper = x
    feedback = ''

    while feedback != 'c':
        if lower != upper:
            guess_number = randint(lower, upper)
        else:
            guess_number = lower
        feedback = input(
            f"\nIs the number {guess_number} Higher(h) OR Lower(l) OR Correct(c)").lower()
        if feedback == 'h':
            upper = guess_number - 1
            continue
        elif feedback == 'l':
            lower = guess_number + 1
            continue
    print("YAY! I won")


guess(20)
