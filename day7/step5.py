import random

words = ["apple", "banana", "mango", "grapes"]

chosen_word = random.choice(words)

display = ["_" for letter in chosen_word]

lives = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the hidden word.")

while "_" in display and lives > 0:

    print("\nWord:", " ".join(display))
    print("Lives:", lives)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:

        print("Correct!")

        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

    else:
        print("Wrong guess!")
        lives -= 1

if lives > 0:
    print("\nCongratulations! You won!")
else:
    print("\nGame Over!")

print("The word was:", chosen_word)
