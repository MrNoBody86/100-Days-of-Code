#Tip calculator Project
 
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

print("Welcome to the tip calculator")
Total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
Num_of_people = int(input("How many people to split the bill? "))

total_tip = Total_bill * percent_tip / 100

Final_bill = Total_bill + total_tip

per_person_split = Final_bill / Num_of_people
#per_person_split = format(Final_bill / Num_of_people,".2f")

print(f"Each person should pay: ${per_person_split:.2f}")

