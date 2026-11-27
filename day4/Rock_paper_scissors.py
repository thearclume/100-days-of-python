import random

rock = "✊"
paper = "✋"
scissors = "✌️"

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 0 and user_choice <= 2:
    print(f"You chose: {game_images[user_choice]}")
else:
    print("You typed an invalid number. You lose!")

computer_choice = random.randint(0, 2)
print(f"Computer chose: {game_images[computer_choice]}")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")
