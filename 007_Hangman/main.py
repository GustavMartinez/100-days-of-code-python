# Import random module
import random

# Simple list of words
word_list = ["aardvark", "baboon", "camel"]

# variable to keep track of the number of lives left
lives = 6

# Using random to select a word
chosen_word = random.choice(word_list)
# print(chosen_word)

# Create a variable with the length of the word 
placeholder = "_" * len(chosen_word)
print(placeholder)


game_over = False

correct_letters = []

while not game_over:


    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"
    print(f"Lives remaining {lives}")

    print(display)


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over=True
        print("You win.")