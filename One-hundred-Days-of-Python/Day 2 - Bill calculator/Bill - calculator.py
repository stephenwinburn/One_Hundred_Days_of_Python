# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:01:51 2022

@author: steph
"""

print("Welcome to the tip calcualtor.")
bill = input("What was the total bill? ")
if bill[0]=="$":
    bill = float(bill[1:])
else:
    bill = float(bill)

people = int(input("How many people split the bill? "))
tip_rate = input("What percentage tip would you like to give? 10, 12, 0r 15? ")
if tip_rate[-1:]=="%":
    clean_tip_rate = float(tip_rate[0:len(tip_rate)-1])
    
if clean_tip_rate % 1 !=0:
    int_tip_rate = int(clean_tip_rate*100)
else: int_tip_rate = int(clean_tip_rate)
    
print("Each person should pay: ${}".format("%.2f" % round(bill*(1+int_tip_rate/100)/people,2)))

