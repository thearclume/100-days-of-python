import random
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#option 1
print(random.choice(friends))

#option 2
random_number = random.randint(0, 4)
print(friends[random_number])