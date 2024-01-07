PLACEHOLDER = "[name]"

with open("Day-20to29\Day-24\project-22-mail-merge\Input\Letters\starting_letter.txt" ) as letter_file:
    letter = letter_file.read()


with open("Day-20to29\Day-24\project-22-mail-merge\Input\\Names\invited_names.txt") as names_file:
    names_list = names_file.readlines()
    for person in names_list :
        stripped_name = person.strip()
        new_letter = letter.replace(PLACEHOLDER,stripped_name)
        with open(f"Day-20to29\Day-24\project-22-mail-merge\Output\ReadyToSend\letter_for_{stripped_name}.txt",mode="w") as new_letter_file:
            new_letter_file.write(new_letter)