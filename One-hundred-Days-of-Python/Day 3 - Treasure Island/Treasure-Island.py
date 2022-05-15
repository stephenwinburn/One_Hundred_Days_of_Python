# -*- coding: utf-8 -*-
"""
Created on Sat May 14 08:44:18 2022

@author: steph
"""

prize = ('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print(prize)
print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")

left_or_right = input('''You\'re at a cross round. 
Where do you want to go?
Type "left" or "right"\n''')

if left_or_right.lower() == 'left':
    wait_or_swim = input('''You came to a lake. 
There is an island in the middle of the lake. 
Type "wait" to wait for a boat.
Type "swim" to swim across.\n''')
    if wait_or_swim.lower() == 'wait':
        three_lights = input('''You arrive at the island unharmed.
There is a house with 3 doors.
One red, one yellow and one blue.
Which color do you choose?\n''')
        if three_lights.lower() == 'yellow':
            print('You won!')
        elif three_lights.lower() == 'red':
            print('Flames engulf all of the room. Game Over.')
        else:
            print('You enter a room of beasts. Game Over.')
    else:
        print('You have been eaten by a crocodile. Game Over')
else:
    print('Game Over')