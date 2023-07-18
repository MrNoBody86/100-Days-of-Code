# You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100

sum_of_even_numbers = 0

for i in range(2,101,2) :
    sum_of_even_numbers += i

print(sum_of_even_numbers)