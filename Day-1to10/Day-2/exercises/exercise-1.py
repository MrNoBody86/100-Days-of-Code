"""Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35, then the output should be 3 + 5 = 8"""

two_digit_number = input("Type a two digit number: ")

# print(type(two_digit_number))

First_digit = two_digit_number[0]
Second_digit = two_digit_number[1]

result = int(First_digit) + int(Second_digit)

print(result)