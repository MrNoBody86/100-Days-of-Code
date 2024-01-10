import pandas

#TODO 1. Create a dictionary in this format : {"A": "Alfa", "B": "Bravo"}
data_nato = pandas.read_csv("Day-20to29\Day-26\project-24-NATO-alphabet\\NATO-alphabet-start\\nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in data_nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

list_of_letters = [letter for letter in input("Enter a word:").upper()]

result = [nato_dict[item] for item in list_of_letters]

print(result)