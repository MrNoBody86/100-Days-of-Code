# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left
# if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

age = input("What is your current age? ")

#print(type(age))

age_as_a_int = int(age)

years_remaining = 90 - age_as_a_int

days_remaining = 365 * years_remaining

weeks_remaining = 52 * years_remaining

months_remaining = 12 * years_remaining

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."

print(message)

