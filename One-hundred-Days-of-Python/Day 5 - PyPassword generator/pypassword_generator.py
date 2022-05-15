# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:33:04 2022

@author: steph
"""

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k',
           'l','m','n','o','p','q','r','s','t','u','v',
           'w','x','y','z','A','B','C','D','E','F','G',
           'H','I','J','K','L','M','N','O','P','Q','R',
           'S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
letter_count = input("How many letters would you like in your password?\n")
symbol_count = input("How many symbols would you like?\n")
number_count = input("How many numbers would you like?\n")

print(f"You chose to have {letter_count} letters, {symbol_count} symbols, and {number_count} numbers in you password.")

password = ''
total_characters = int(letter_count)+int(symbol_count)+int(number_count)
characters_used = 0
letters_used = 0
symbols_used = 0
numbers_used = 0

for i in range(1,total_characters+1):
    character_type = random.randint(0,2)
    if character_type == 0: 
        if letters_used < int(letter_count) and characters_used < total_characters:
            password = password + random.choice(letters)
            letters_used += 1
            i += 1
            characters_used += 1
        else:
            pass 
    elif character_type == 1 and characters_used < total_characters:
        if numbers_used < int(number_count):
            password = password + random.choice(numbers)
            numbers_used += 1
            i += 1
            characters_used += 1
        else:
            pass 
    else:
        if symbols_used < int(symbol_count) and characters_used < total_characters:
            password = password + random.choice(symbols)
            symbols_used += 1
            i += 1
            characters_used += 1
        
    




print(f"Here is your password: {password}")