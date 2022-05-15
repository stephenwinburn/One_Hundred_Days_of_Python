# -*- coding: utf-8 -*-
"""
Created on Sun May 15 08:50:37 2022

@author: steph
"""

import random

skull_and_crossbones = """            .-.
           (0.0)
         '=.|m|.='
         .='`"``=."""

play_dict = {"0":("Rock","""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""),
             "1":("Paper","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""),
             "2":("Scissors","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")}

# User action
user_number = input("Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
if user_number not in play_dict:
    play_dict[user_number] = ("You have chosen poorly.",skull_and_crossbones)
user_choice = play_dict[user_number][0]
user_picture = play_dict[user_number][1]
print(f"You chose: {user_choice}")
print(f"{user_picture}\n")

# Computer action
computer_number = str(random.choice([0,1,2]))
computer_choice = play_dict[computer_number][0]
computer_picture = play_dict[computer_number][1]
print(f"The computer chose: {computer_choice}")
print(f"{computer_picture}\n")
      
# Deciding the winner
if int(user_number) not in [0,1,2]:
    print("You chose an invalid value. You lose!")
elif user_choice == 0:
    if computer_choice == 0: 
        print("The game is a draw.")
    elif computer_choice == 1:
        print("The computer wins. Paper beats rock.")
    else:
        print("You win! Rock beats scissors.")
elif user_choice == 1:
    if computer_choice == 0: 
        print("You win! Paper beats rock.")
    elif computer_choice == 1:
        print("The game is a draw.")
    else:
        print("The computer wins. Scissors beat paper.")
else: 
    if computer_choice == 0: 
        print("The computer wins. Rock beats scissors.")
    elif computer_choice == 1:
        print("You win! Scissors beat paper.")
    else:
        print("The game is a draw.")
        
# Allow the user to continue to play?


