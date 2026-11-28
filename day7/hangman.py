#project7
import random

# List of words for the game
words = ["apple", "banana", "mango", "grapes", "python", "coding"]

# Select a random word
chosen_word = random.choice(words)

# Create blanks for each letter
display = ["_" for letter in chosen_word]

# Set the player's lives
lives = 6

# Store guessed letters
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the hidden word.")

# Continue while the word is incomplete and lives remain
while "_" in display and lives > 0:

    print("\nWord:", " ".join(display))
    print("Lives remaining:", lives)

    guess = input("Guess a letter: ").lower()

    # Check whether the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the guessed letter is in the word
    if guess in chosen_word:
        print("Correct guess!")

        # Reveal all matching letters
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

    else:
        print("Wrong guess!")
        lives -= 1

# Display the final result
if "_" not in display:
    print("\nCongratulations! You won!")
else:
    print("\nGame Over!")

print("The word was:", chosen_word)
