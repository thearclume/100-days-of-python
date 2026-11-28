import random

words = ["apple", "banana", "mango", "grapes"]

chosen_word = random.choice(words)

display = ["_" for letter in chosen_word]

lives = 6

while "_" in display and lives > 0:

    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives = lives - 1
        print("Wrong guess!")
        print("Lives remaining:", lives)

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    print(display)

if lives == 0:
    print("Game Over!")
    print("The word was:", chosen_word)
else:
    print("You won!")
