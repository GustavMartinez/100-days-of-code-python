#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



LETTER_PATH = "024_2_mail_merge/Input/Letters/starting_letter.txt"
NAMES_PATH = "024_2_mail_merge/Input/Names/invited_names.txt"
PATH_TO_SAVE = "024_2_mail_merge/Output/ReadyToSend/"

all_names = []

with open(NAMES_PATH, mode='r') as names_file:
    names_content = names_file.readlines()
    
    for i in names_content:
        i = i.strip()
        #i = i.upper()
        all_names.append(i)


for j in all_names:
    with open(LETTER_PATH, mode="r") as letter_file:
        letter_content = letter_file.read()
        letter_content = letter_content.replace("[name]", j)
        with open(f"{PATH_TO_SAVE}/{j}", 'w') as new_file:
            new_file.write(letter_content)






