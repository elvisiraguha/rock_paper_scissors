from optparse import OptionConflictError
import re
import random

from click import Option


options = {"R": "Rock", "P": "Paper", "S": "Scissors"}


def win(players):
    if players["Player"] == 'S':
        if players["Computer"] == 'P':
            print("Player")

        if players["Computer"] == 'R':
            print("Computer")

    if players["Player"] == 'R':
        if players["Computer"] == 'P':
            print("Computer")

        if players["Computer"] == 'S':
            print("Player")

    if players["Player"] == 'P':
        if players["Computer"] == 'S':
            print("Computer")
            
        if players["Computer"] == 'R':
            print("Player")


user_choice = ""

while True:
    user_choice = input("Enter your choice ('R', 'P', 'S'): ")

    if not re.search('[RPS]', user_choice):
        continue

    computer_choice = random.choice([k for k, v in options.items()])

    print("Player ({0}) : CPU ({1})".format(
        options[user_choice], options[computer_choice]))

    if(computer_choice == user_choice):
        user_choice = ""
    else:
        win({"Player": user_choice, "Computer": computer_choice})
        break
