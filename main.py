#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3screhools.com/python/f_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    name = names_file.readlines()

for item in name:
    new_letter = letter.replace("[name]", item.strip())
    with open(f"./Output/ReadyToSend/letter_{item.strip()}.txt", mode="w") as file:
        file.write(new_letter)


