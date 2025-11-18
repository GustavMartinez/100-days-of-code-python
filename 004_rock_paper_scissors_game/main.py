import random

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("")
print("WELCOME TO THE ROCK, PAPER, SCISSORS GAME!")
print("")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

options = ["Rock", "Paper", "Scissors"]

user_choose = int(input("What do you choose?, Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choose = random.randint(0, 2)


print(f"User choose: {options[user_choose]}")
print(f"Computer choose: {options[pc_choose]}")


if user_choose == 0 and pc_choose == 2:
    print("You won")
elif user_choose == 1 and pc_choose == 0:
    print("You won")
elif user_choose == 2 and pc_choose == 1:
    print("You won")
elif user_choose == pc_choose:
    print("Draw")
else:
    print("You lose!, Computer won")