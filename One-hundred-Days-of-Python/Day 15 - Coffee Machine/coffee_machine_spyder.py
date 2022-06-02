# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:34:59 2022

@author: steph
"""

import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": [300, 'ml'],
    "milk": [200, 'ml'],
    "coffee": [100, 'g']
}

coins = {
    "quarter": [0.25, 0],
    "dime": [0.1, 0],
    "nickel": [0.05, 0],
    "penny": [0.01, 0]
}

bank = {"Money": 0.00}


def run_report():
    for key in resources:
        print(f"We have {resources[key][0]}{resources[key][1]} of {key} available.")

    print(f"Money: ${bank['Money']}")
    
    return ''


def select_drink():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == 'report':
        print(run_report())
    if drink == 'off':
        sys.exit([drink == 'off'])
    else:
        return drink


def drink_ingredients(drink):
    if drink == 'report':
        pass
    else:
        return [MENU[drink]['ingredients']['water'],
                MENU[drink]['ingredients']['milk'],
                MENU[drink]['ingredients']['coffee']]


def check_resources(drink):
    if drink == 'report':
        pass
    else:
        drink_resources = drink_ingredients(drink)
    
        for key, value in resources.items():
            for i in range(0, 2):
                if drink_resources[i] > value[0]:
                    return print(f"Insufficient resources. There is not enough {key}")
    
            return True


def total_user_coins():
    user_coins = [0, 0, 0, 0]    

    print("Please insert coins.")
    user_coins[0] = input("How many quarters?")
    user_coins[1] = input("How many dimes?")
    user_coins[2] = input("How many nickles?")
    user_coins[3] = input("How many pennies?")

    user_paid = 0
    i = 0
    for key, value in coins.items():
        user_paid += float(value[0])*int(user_coins[i])
        i += 1

    return user_paid


def update_bank(drink_cost):
    bank['Money'] += drink_cost



# Here we could make this more flexible since dictonaries are order preserving.
# We could cycle through keys. This would allow expanded ingrediants if our
# drink menu added new items.
def update_resources(ingredients,drink):
    resources['water'][0] -= ingredients[0]   
    resources['milk'][0] -= ingredients[1]
    resources['coffee'][0] -= ingredients[2]


def process_drink_order(drink):
    if check_resources(drink):
        user_paid = total_user_coins()
        drink_cost = MENU[drink]['cost']
        ingredients = drink_ingredients(drink)
        if  user_paid > drink_cost:
            print(f"Your change is ${user_paid - drink_cost}.")
            print(f"Here is your {drink}. Enjoy!")
            update_bank(drink_cost)
            update_resources(ingredients,drink)
            return True
        elif user_paid == drink_cost:
            print(f"Here is your {drink}. Enjoy!")
            update_bank(drink_cost)
            update_resources(ingredients,drink)
            return True
        else:
            return print("Sorry, that is not enough money. Money returned.")

def drink_loop():    
    drink =select_drink()
    process_drink_order(drink)
    drink_loop()
    
drink_loop()


