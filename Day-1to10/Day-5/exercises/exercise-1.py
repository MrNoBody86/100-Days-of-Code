# You are going to write a program that calculates the average student height from a List of heights.

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

number_of_student = 0
total_height = 0

for height in student_heights :
    number_of_student += 1
    total_height += height

average_height = round(total_height / number_of_student)

print(average_height)