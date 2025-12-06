# Importar la biblioteca
import random

# Lista de las cartas en el set de cartas
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print()


def play():
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \t")
    
    if game == 'y':
        return True
    else:
        return False




while play():

    # Creacion de la lista de las cartas del computador y el usuario. listas vacias
    player_hand = []
    computer_hand = []


    # seleccion aleatoria de las cartas iniciales del pc y del jugador
    for _ in range(2):
        player_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))


    # condicion para que el computador elija una carta mas, si las actuales cartas suman menos que 17
    while sum(computer_hand) < 17:
        computer_hand.append(random.choice(cards))

        while sum(computer_hand) > 21 and 11 in computer_hand:
            computer_hand.remove(11)
            computer_hand.append(1)



    # Condicion para que el usuario elija o no más cartas e indique si se paso de 21

    more_cards = True

    while more_cards:

        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}") # >>>>>>>>>>>>>>>>>>>>>> print
        print(f"computer's firts card: {computer_hand[0]}") # mostrar la primera carta del pc # >>>>>>> print
        
        add = input("Try 'y' to get another card, type 'n' to pass: \t")


        if add == 'y':
            player_hand.append(random.choice(cards))
            while sum(player_hand) > 21 and 11 in player_hand:
                player_hand.remove(11)
                player_hand.append(1)


        elif add == 'n':
            more_cards = False
            print(f"Your final hand: {player_hand}, final score is {sum(player_hand)}")
            print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
            if sum(computer_hand) > 21:
                print("Opponent went over. You win! ")
            elif sum(player_hand) > sum(computer_hand):
                print("You win!")
            elif sum(player_hand) == sum(computer_hand):
                print("tie!")
            else:
                print("Computer wins")


        if sum(player_hand) > 21:
            more_cards = False
            print(f"Your final hand: {player_hand}. Your final score is {sum(player_hand)}")
            print(f"Computer's final hand: {computer_hand[0]}, final score: {computer_hand[0]}")
            print(f"You went over. You lose")


