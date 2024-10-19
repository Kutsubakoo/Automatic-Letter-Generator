with open("./Input/Names/invited_names.txt", "r") as names:
    extracted_names = names.readlines() # readlines() to extract all the names

with open("./Input/Letters/starting_letter.txt") as letter:
    start_letter = letter.read()


for name in extracted_names:
    remove_whitespace = name.strip()
    updated_letter = start_letter.replace("[name]", remove_whitespace) #replace() to replace [name] with real name from list
    with open(f"./Output/ReadyToSend/Letter_For_{remove_whitespace}.docx", "w") as process:
        process.write(updated_letter)