fruits = ["apple", "banana", "pear", "peach"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)


student_scores = {101: 90, 102: 80, 103: 70, 104: 60}
total_score = sum(student_scores.values())
sum = 0
for score in student_scores.values():
    sum += score
print(f"Total score: {sum}")


for score in student_scores.values():
    if score > max(student_scores.values()):
        print(f"Highest score: {score}")