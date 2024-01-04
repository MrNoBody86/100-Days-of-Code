# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# BMI = weight / height^2


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


#print(type(height))

height_2 = float(height)


BMI = weight / height_2 ** 2

new_BMI = int (BMI)

print(new_BMI)