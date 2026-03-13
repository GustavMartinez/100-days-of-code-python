"""
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Todo 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# Todo 2. Create a list of the phonetic code words from a word that the user inputs.

"""

import pandas as pd

PATH_FILE = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_26/day_project/nato_phonetic_alphabet.csv'

file = pd.read_csv(PATH_FILE)


# Dictionary comprehension to convert dataframe in dictionary
data = {row.letter:row.code for (index, row) in file.iterrows()}


# list comprehension to create a list of letters from a user word
user_word = [i.upper() for i in input("Enter a word: ")]


# Conditional list comprehension to create a list with the correspondent word from the Nato alphabet
nato_list = [data.get(letter) for letter in user_word if letter in data.keys()]

print(nato_list)