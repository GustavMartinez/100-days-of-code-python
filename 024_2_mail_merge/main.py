#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



LETTER_PATH = "024_2_mail_merge/Input/Letters/starting_letter.txt"
NAMES_PATH = "024_2_mail_merge/Input/Names/invited_names.txt"

with open(LETTER_PATH, mode='r') as letter_file:
    letter_content = letter_file.read()
    print(letter_content)


with open(NAMES_PATH, mode='r') as names_file:
    names_content = names_file.read()
    print(names_content)


