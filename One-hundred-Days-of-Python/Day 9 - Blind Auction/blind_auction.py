# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:29:04 2022

@author: steph
"""

import gavel

# This is needed for Spyder console clear
# The lesson uses from replit import clear, which we do not have.
from IPython import get_ipython

# If we have bidders with the same name we append their 
# order in the bid among those with identical names.
def duplicate_bidder(new_bidder,bid_dict):
    i=2
    iter_list = []
    while new_bidder in bid_dict:
        iter_list.append(i)
        replacement_bidder = new_bidder+str(iter_list[-1])
        new_bidder = replacement_bidder
        i += 1
        
    return new_bidder

def add_bidder(bid_dict):
    additional_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if additional_bidders == 'yes':
        get_ipython().magic('clear')
        new_bidder = input("What is your name?: ")
        new_bidder = duplicate_bidder(new_bidder,bid_dict)
        new_bid = float(input("What's your bid?: $"))
        bid_dict[new_bidder] = new_bid
        add_bidder(bid_dict)
    else:
        return bid_dict
    
def reveal_bids(bid_dict):
    for key,value in bid_dict.items():
        print(key,value)
        
    return ''         

print(gavel.gavel,"\n")
print("Welcome to the secret auction program.")
initial_bidder = input("What is your name?: ")
initial_bid = float(input("What's your bid?: $"))

bid_dict = {}
bid_dict[initial_bidder] = initial_bid
add_bidder(bid_dict)

max_bid = 0
winning_bidder = 'Tallying bids'

max_bids = {}

for key, value in bid_dict.items():
    if value > max_bid:
        max_bid = value
    else:
        pass

# Here we have allowed for the possibility of tied maximum bids.
# In such a case, the earliest bidder wins.
max_bids_list = []
for key,value in bid_dict.items():
    if value == max_bid:
        max_bids_list.append(key)
    else:
        pass
    
   
print(f"\n{max_bids_list[0]} won the auction with a bid of ${max_bid}.\n")
print(f"The bids considered were:\n ")
print(reveal_bids(bid_dict))
        
        
    