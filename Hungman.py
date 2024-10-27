import random
import time
from Words import word_list

word = random.choice(word_list)
word_length = len(word)
word_leters = list(word)
fillin = ['_'] * word_length
guess = word_length


print(f"The random word has {word_length} characters and you have {word_length} letters asw")
print(''.join(fillin))

while '_' in fillin and guess > 0:
    letter = input("Enter a letter ")
    if letter in word_leters:
        print("Very good, you guessed it correct")
        for i in range(word_length):
            if letter == word_leters[i]:
                fillin[i] = letter
    else:
        print(f"Make another try, you have {guess - 1} more guesses left")
        guess -= 1
    print(''.join(fillin))
    time.sleep(2)

print("Wow completed " if guess > 0 else f"You failed nigga, the word was {word}")
