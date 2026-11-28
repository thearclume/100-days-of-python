import random

words = ["apple", "banana", "mango", "grapes"]

chosen_word = random.choice(words)

guess = input("Guess a letter: ").lower()

if guess in chosen_word:
    print("Correct guess!")
else:
    print("Wrong guess!")

print("The word was:", chosen_word)
