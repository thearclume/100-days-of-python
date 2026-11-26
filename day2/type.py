## TypeError: object of type 'int' has no len()
#len(1234)

print(len("1234"))
print(len("hello"))
print(type("hello"))
print(type(1234))
print(type(12.34))
print(type(True))

#canatination - means joining two strings together
print("hello" + " " + "world")
print("1234" + "5678")

#type conversion - converting one data type to another
print(int("1234") + int("5678"))


#exercise
#print("number of characters in your name is " + (len(input("What is your name? "))))
#here we are trying to concatenate a string with an integer, which is not allowed in Python. 
#We need to convert the integer to a string first.
#so we can fix the above line of code by converting the integer to a string using the str() function.
#Here's the corrected code:

#print("number of characters in your name is " + str(len(input("What is your name? "))))


name_of_the_user = input("What is your name? ")
length_of_name = len(name_of_the_user)

print(type(name_of_the_user))
print(type(length_of_name))
print("number of characters in your name is " + str(length_of_name))      