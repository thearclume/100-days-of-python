import random

words = ["apple", "banana", "mango", "grapes"]

chosen_word = random.choice(words)

display = ["_" for letter in chosen_word]

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    print(display)

print("You won!")
