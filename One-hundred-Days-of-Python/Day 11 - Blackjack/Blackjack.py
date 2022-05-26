# -*- coding: utf-8 -*-
"""
Created on Wed May 25 11:22:51 2022

@author: steph
"""

import Blackjack_art
import random

card_value_dict = {'A':11,
                   'A1':1,
                   '2':2,
                   '3':3,
                   '4':4,
                   '5':5,
                   '6':6,
                   '7':7,
                   '8':8,
                   '9':9,
                   '10':10,
                   'J':10,
                   'Q':10,
                   'K':10}

card_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def deal_card(hand):    
    hand.append(random.choice(card_list)) 
        
    return hand

def deal_hand():
    hand = []
    for i in range(0,2):
        deal_card(hand)
        
    return hand

def score_hand(hand):
    score_list = []
    for item in hand:
        score_list.append(card_value_dict[item])
        
    return sum(score_list)

def bust(hand):
    if 'A' in hand:
        aces_available = hand.count('A')
        while score_hand(hand) > 21 and aces_available > 0:
            hand[hand.index('A')] = 'A1'
            aces_available -= 1
        print(f"Your hand, {hand}, has a total score of {score_hand(hand)}.")
        hit_or_stay(hand)
    else:
        print(f"Your hand {hand} has a total of {score_hand(hand)}. You busted.")
        play_blackjack(input("Would you like to play a game of Blackjack? Type 'y' or 'n': "))
        
    return hand

def hit_or_stay(hand):

    hit = input("Type 'y' to get another card. Type 'n' to pass.")
    if hit == 'n':
        return print(f"You chose to stick with the hand {hand}.")
    
    else:
        hand.append(random.choice(card_list))
        print(f"Your hand is {hand}.")
        if score_hand(hand) > 21:
            bust(hand)
        else:            
            hit_or_stay(hand)
        return hand       

def play_blackjack(play_a_game = 'n'):
    
    if play_a_game == 'n':
        return print("Thank you for playing Blackjack with me.!")
    
    else:
        player_hand = deal_hand()   
        print(f"Your hand: {player_hand} \n")    
        
        if score_hand(player_hand) == 21 and 'A' in player_hand:
            print(f"BLACKJACK! You win with the hand {player_hand}.")
            play_blackjack(input("\nWould you like to play another game of Blackjack? Type 'y' or 'n': "))
        
        dealer_hand = deal_hand()         
        print(f"First card of dealer hand: {dealer_hand[0]} \n")
        
        if score_hand(dealer_hand) == 21 and 'A' in dealer_hand:
            print(f"BLACKJACK! The dealer wins with the hand {dealer_hand}.")
            play_blackjack(input("\nWould you like to play another game of Blackjack? Type 'y' or 'n': "))
        
        (hit_or_stay(player_hand))
        
        if score_hand(player_hand) < 21:
            while score_hand(dealer_hand) <= 12:
                deal_card(dealer_hand)
                print("Dealer took a card.")
                if score_hand(dealer_hand) > 21 and 'A' in dealer_hand:
                    bust(dealer_hand)
                if score_hand(dealer_hand) > 21 and 'A' not in dealer_hand:
                    print("Dealer busts. You win!")
                    play_blackjack(input("Would you like to play a game of Blackjack? Type 'y' or 'n': "))
        
        if score_hand(dealer_hand) < score_hand(player_hand) < 22:
            print(f"You win with score {score_hand(player_hand)} and cards {player_hand}!")
            print(f"The dealer score was {score_hand(dealer_hand)} on the hand {dealer_hand}.")                         
        elif score_hand(player_hand) < score_hand(dealer_hand) < 22:
            print(f"Dealer wins with score {score_hand(dealer_hand)} and cards {dealer_hand}!")
        else:
            print("It looks like a draw to me.")
            print(f"The dealer score was {score_hand(dealer_hand)} on the hand {dealer_hand}.")
        
    play_blackjack(input("\nWould you like to play another game of Blackjack? Type 'y' or 'n': "))
    

print(Blackjack_art.blackjack_text)
  
play_blackjack(input("Would you like to play a game of Blackjack? Type 'y' or 'n': "))
    