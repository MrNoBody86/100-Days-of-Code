# with open("Day-20to29\Day-25\weather_data.csv",mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day-20to29\Day-25\weather_data.csv",mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data :
#         if row[1] != "temp" :
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas as pd

# data = pd.read_csv("Day-20to29\Day-25\weather_data.csv")

# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg = data["temp"].mean()
# print(avg)

# largest = data["temp"].max() 
# print(largest)

# Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# temp_in_fahrenheit = monday.temp[0] *9/5 +32
# print(temp_in_fahrenheit)


#Create a dataframe from scratch

# data_dict = {
#     "student":["Amy","James","Angela"],
#     "scores" : [76,56,65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("Day-20to29\Day-25\\new_data.csv")

# squirrel_data = pd.read_csv("Day-20to29\Day-25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240107.csv")

# primary_fur_color = squirrel_data["Primary Fur Color"]

# data = primary_fur_color.value_counts()

# df = pd.DataFrame(data)

# df.to_csv("Day-20to29\Day-25\Squirrel_Primary_Fur_Color_Data.csv")

#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("Day-20to29\Day-25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240107.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Day-20to29\Day-25\Squirrel_Primary_Fur_Color_Data.csv")