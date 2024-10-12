#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#readlines() to extract all the names
#replace() to replace [name] with real name from list
#strip()???

with open("./Input/Names/invited_names.txt", "r") as names:
    extracted_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    start_letter = letter.read()


for name in extracted_names:
    remove_whitespace = name.strip()
    updated_letter = start_letter.replace("[name]", remove_whitespace)
    with open(f"./Output/ReadyToSend/Letter_For_{remove_whitespace}.docx", "w") as process:
        process.write(updated_letter)