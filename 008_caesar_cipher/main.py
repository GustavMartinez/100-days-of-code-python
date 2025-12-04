alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, original_text, shift_amount):

    def encrypt(original_text, shift_amount):

        encrypted = ""

        for letter in original_text:
            position = alphabet.index(letter) + shift_amount
            position %= len(alphabet)
            encrypted += alphabet[position]

        print(f"Here is the encoded result: {encrypted}")


    def decrypt(original_text, shift_amount):
        
        decrypt = ""
        
        for i in original_text:
            position = alphabet.index(i) - shift_amount
            position %= len(alphabet)
            decrypt = decrypt + alphabet[position]
        print(decrypt)


    if direction == "encode":
        encrypt(original_text, shift_amount)
    
    elif direction == "decode":
        decrypt(original_text, shift_amount)

    else:
        print("No funciono")



again = True

while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)


    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    
    if restart == 'yes':
        again = True
    else:
        again = False

