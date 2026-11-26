print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


#explanation of the code above
# This code calculates the total cost of a pizza order based on the size, pepperoni, and extra cheese options selected by the user.
#workflow of the code:
# 1. The program starts by printing a welcome message to the user.
# 2. It prompts the user to input their desired pizza size (S, M, or L), whether they want pepperoni (Y or N), and whether they want extra cheese (Y or N).
# 3. The program initializes a variable called bill to 0, which will be used to keep track of the total cost of the order.
# 4. It uses if/elif statements to determine the base cost of the pizza based on the size selected by the user. The cost is added to the bill variable.
# 5. The program checks if the user wants pepperoni. If they do, it adds the appropriate cost to the bill based on the size of the pizza.
# 6. It checks if the user wants extra cheese. If they do, it adds $1 to the bill.
# 7. Finally, the program prints the final bill amount to the user using an f-string to format the output.
