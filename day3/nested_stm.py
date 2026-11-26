print("welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    #indentation is very important in python
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    bill = 0
    #this is a nested if statement, an if statement inside another if statement
    if age < 12:
        print("Please pay $5.")
        bill = 5
    elif age <= 18:
        print("Please pay $7.")
        bill = 7
    else:
        print("Please pay $12.")
        bill = 12
    want_photo = input("Do you want a photo taken? y or n. ")
    if want_photo == "y":
        bill += 3
        print(f"You have to pay an additional $3 for the photo. Your total is ${bill}.")
    else:
        print(f"Your total is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
