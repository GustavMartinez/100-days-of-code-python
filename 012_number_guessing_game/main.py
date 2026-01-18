print()
print("************************************")
print("Welcome to the Number Guessing Game!")
print("************************************")
print()
print("I'm thinking of a number between 1 and 100.")


import random

def game(attemps):
    pc_number = random.randint(1,100)
    user_attempts = attemps

    game_on = True

    while game_on:
        if user_attempts > 0:
            # print(f"The pc number is {pc_number}")
            print(f"You have {user_attempts} attemps remaining to guess the number")

            user_guess = int(input('Make a guess: '))

            if pc_number == user_guess:
                print(f"You got it! The answer was {pc_number}")
                game_on = False

            elif user_guess > pc_number:
                user_attempts -= 1
                print("Too high")
                print("Guess again")

            else:
                user_attempts -= 1
                print("Too low")
                print("Guess again")
        else:
            print("You lose!")
            game_on = False


def user_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        game(10)
    elif difficulty == 'hard':
        game(5)
    else:
        print("Not valid comand")


user_difficulty()