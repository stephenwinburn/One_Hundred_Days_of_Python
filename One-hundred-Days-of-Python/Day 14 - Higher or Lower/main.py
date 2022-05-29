# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:41:50 2022

@author: steph
"""

import random
import game_data
import art
# from IPython import get_ipython

def play_game():
    return input("Would you like to play Higher-Lower? Type 'y' to play and 'n' to exit.")

def choose_challenger(champion):
    challenger = random.choice(game_data.data)
    if champion == challenger:
        choose_challenger(champion)
    else:
        return challenger
    
def compare_champion_challenger(champion,challenger):
    if champion['follower_count'] > challenger['follower_count']:
        return 'A'
    else:
        return 'B'
    
    
print(art.logo)

def play_high_low():
    champion = random.choice(game_data.data)
    play = 'y'
    score = 0
    while play == 'y':       
        
        print(f"Compare A: {champion['name']}, a {champion['description']}, from {champion['country']}.")
        print("\n")
        print(art.vs)
        print("\n")
        challenger = choose_challenger(champion)
        print(f"Against: {challenger['name']}, a {challenger['description']}, from {challenger['country']}.")
        user_guess =input("Who has more followers? Type 'A' or 'B'.").upper()
        if user_guess == compare_champion_challenger(champion,challenger):
            print("Congratulations! You chose correctly.")
            score += 1
            print(f"Your current score is {score}.")
            champion = challenger
            play = play_game()
        else:
            print(f"I'm sorry, you chose incorrectly. Your score was {score}.")
            champion = challenger
            play = play_game()
            
play_high_low()