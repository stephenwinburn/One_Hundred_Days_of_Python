# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:42:57 2022

@author: steph
"""

import random
import HangmanStages as HMS
import HangmanIntro

print(HangmanIntro.hangman)

word_bank = ['biscuit','superman','cat','tree',
              'house','bug','speckles','hug',
              'whisper']

# word_bank = ['treeeee']

word_to_guess = list(random.choice(word_bank))


blank_list = []
for char in word_to_guess:
    blank_list += '_'

    
print(f"Can you guess which word this is {blank_list}?")
print(f"The word contains {len(word_to_guess)} letters.")

i = 0
while '_' in blank_list:
    letter_guess = input("Guess a letter!\n").lower()
    if letter_guess in blank_list:
        print(f'You have already guessed {letter_guess}')
    elif letter_guess not in word_to_guess:
        if i != len(HMS.hang)-1:
            print('oops')
            print(HMS.hang[i])
            i += 1 
        else:
            print('You failed to guess the word')
            break
    # Here condition on the guess being in the word,
    # and there being a blank at the index point     
    else:
        while letter_guess in (word_to_guess):
            ind = word_to_guess.index(letter_guess)
            blank_list[ind]=word_to_guess[ind]
            word_to_guess[ind] ='_'
            
        print(f"\n {''.join([str(item) for item in blank_list])}")
        
if '_' not in blank_list: 
    print(f"\nCongratulations! You guessed the word {''.join([str(item) for item in blank_list])} correctly\n")
    for i in range(0,2*len(HMS.celebrate)):
        print(HMS.celebrate[i%2])
        
        
        
        
        