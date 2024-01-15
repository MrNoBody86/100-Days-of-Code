import pandas


data_nato = pandas.read_csv("Day-20to29\\Day-26\\project-24-NATO-alphabet\\NATO-alphabet-start\\nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in data_nato.iterrows()}

def nato_phonetic_alphabet():
    input_str = input("Enter a word:").upper()
    try :
        result = [nato_dict[item] for item in input_str]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_phonetic_alphabet()
    else:
        print(result)

nato_phonetic_alphabet()