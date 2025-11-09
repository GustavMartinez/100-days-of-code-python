print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \..  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\p||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\p/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

    ''')

# ascci art: https://ascii.co.uk/art

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
choise_1 = input("\t Type 'left' or 'right':\n").lower()

if choise_1 == 'left' or choise_1 == 'Left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    choise_2 = input("\t Type 'wait' to wait for the boat. Type 'swim' to swim across. \n").lower()

    if choise_2 == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one blue, one yellow.")
        choise_3 = input("\t Which colour do you choose? \n").lower()

        if choise_3 == 'blue' or choise_3 == 'red':
            print("Game over")
        elif choise_3 == 'yellow':
            print("You win")

    else:
        print("Game over")

elif choise_1 == 'right' or choise_1=='Right':
    print("Game over")

