# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)

print(int(bmi)) #this will print the integer value of bmi
print(round(bmi)) #this will print the rounded value of bmi
print(round(bmi, 2)) #this will print the rounded value of bmi to 2 decimal places
bmi = round(bmi)



#operators
#assignment operator - means assigning a value to a variable
score = 0
score += 1 #this is the same as score = score + 1
print(score)

#f-strings - means formatting strings
print("your score is " + str(score)) #this will print the value of score in the string
print(f"your score is {score}") #this will print the value of score in the string

print(f"your score is {score} and your bmi is {bmi}")
#this will print the value of score and bmi in the string

#quiz
print(6 + 4 / 2 - (1 * 2))
#ans - 6.0
a = int("5") / int(2.7)
print(a)
#ans - 2.5
