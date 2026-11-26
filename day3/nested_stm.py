print("welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    #indentation is very important in python
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    #this is a nested if statement, an if statement inside another if statement
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
