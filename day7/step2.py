import random

words = ["apple", "banana", "mango", "grapes"]

chosen_word = random.choice(words)

display = []

for letter in chosen_word:
    display.append("_")

print(display)

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        display[position] = guess

print(display)
