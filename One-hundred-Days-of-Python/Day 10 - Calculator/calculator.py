# -*- coding: utf-8 -*-
"""
Created on Mon May 23 06:53:01 2022

@author: steph
"""

import calc_art

def add(x,y):
    return float(x) + float(y)

def subtract(x,y):
    return float(x) - float(y)

def multiply(x,y):
    return float(x) * float(y)

def divide(x,y):
    try:
        return float(x) // float(y)
    except ZeroDivisionError:
        print("Error: Division by zero.")   
        
operand_dict = {"+":add,
                "-":subtract,
                "*":multiply,
                "/":divide
                }
        
def tally_result(continue_result,op_call):
    
    if continue_result == 'no':
        f_number = input("What is your first number? ")
        print("\n")
        print(calc_art.operators)
        operation = input("Pick an operation from above please. ")
        s_number = input("What is your second number? ")
    else:
        f_number = op_call
        print("\n")
        print(calc_art.operators)
        operation = input("Pick an operation from above please. ")
        s_number = input("What is your second number? ")       
    
    for key in operand_dict:
        if operation == key:
            op_call = operand_dict[key](f_number,s_number)
            print(f"{float(f_number)} {operation} {float(s_number)} = {op_call}\n")
    
    continue_result = input("Please enter 'yes' or 'no' to indicate if you would like to continue calcuating with your prior result.\nEnter 'exit' to quit. ")
    if continue_result == 'yes':
        tally_result(continue_result,op_call)  
    elif continue_result == 'no':
        tally_result(continue_result,op_call)
    else: 
        return print("Thank you for playing!")
    
print(calc_art.calculator_art)
print("Welcome to the calcuator!\n")
   
tally_result(continue_result = 'no',op_call = 0)



    