import random

def guess(x):
    l = 1
    u = x
    guesses = 1
    while True:
        guess = random.randint(l, u)
        ask = input(f"Is {guess}, the right num? (y/n)")
        if ask == "y":
            print(f"Yayyyyy, I guessed the right num in {guesses} tries")
            break
        elif ask == 'n':
            loworhigh = input("Is your guess higher or lower (h/l)")
            if loworhigh == 'h':
                l = guess + 1
            elif loworhigh == 'l':
                u = guess - 1
        guesses += 1

guess(20)