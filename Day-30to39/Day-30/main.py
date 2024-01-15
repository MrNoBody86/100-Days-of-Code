# FileNotFound

try:
    file = open("Day-30to39\\Day-30\\a_file.text", encoding="utf-8")
    a_directory = {"key":"value"}
    print(a_directory["key"])
except FileNotFoundError:
    file = open("Day-30to39\\Day-30\\a_file.text","w", encoding="utf-8")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This a error that i made up")

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
