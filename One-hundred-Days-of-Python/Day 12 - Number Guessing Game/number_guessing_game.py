# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:54:23 2022

@author: steph
"""

import random

def decrement_guesses(number_of_guesses):
    number_of_guesses -= 1
    return number_of_guesses

def evaluate_guess(guess,number_i_thought_of,number_of_gueses):
    if guess < number_i_thought_of:
        print("Too low")
        return decrement_guesses(number_of_guesses)
    elif guess > number_i_thought_of:
        print("Too high")        
        return decrement_guesses(number_of_guesses)
    else: 
        return -1

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

play_again = 'y'

while play_again == 'y':
    if input("Choose a difficulty level. Type 'easy' or 'hard': ") == 'easy':
        number_of_guesses = 10
    else:
        number_of_guesses = 5
        
    number_i_thought_of = random.randint(1,101)
    
    while number_of_guesses > 0:
        guess = int(input("Make a guess: "))
        number_of_guesses = evaluate_guess(guess,
                                           number_i_thought_of,
                                           number_of_guesses)
    if number_of_guesses == -1:
        print(f"You've guessed the number I was thinking of, {number_i_thought_of}, correctly")
        
    if number_of_guesses == 0:
        print("You've run out of guesses, you lose.")
        
    play_again = input("Type 'y' if you would like to play again? Otherwise, type 'n'")
    
print("Thank you for taking the time to play a game with me.")
    