#project 2 - tip calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
total_bill_indian = total_bill * 90
print(f"The total bill in Indian Rupees is: ₹{total_bill_indian}")
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_amount = total_bill * tip / 100
total_bill_with_tip = total_bill + tip_amount
bill_per_person = total_bill_with_tip / people
print(f"Each person should pay: ${bill_per_person:.2f}")
