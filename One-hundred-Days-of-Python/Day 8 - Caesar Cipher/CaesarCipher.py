# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:25:44 2022

@author: steph
"""
# Consistent with other projects, I always attempt to code
# the porject and plug holes before watching the videos

import CaesarGreeting

# Root vocabulary that cipher will shift
vocabulary = ['a','b','c','d','e','f','g','h','i','j',
              'k','l','m','n','o','p','q','r','s','t',
              'u','v','w','x','y','z']

print(CaesarGreeting.Intro)



# Replaced the two functions below with a single function
# def encode_word(message_in,shift_distance=1):
#     vocab_lexicon = vocabulary[shift_distance:] + vocabulary[:shift_distance]
#     encode_cipher = dict(zip(vocabulary,vocab_lexicon))
#     message_in_list = list(message_in)
#     message_out_list = ['-']*len(message_in_list)
#     for i in range(0,len(message_in_list)):
#         if message_in_list[i] in vocabulary:
#             message_out_list[i] = encode_cipher[message_in_list[i]]
#         else:
#             message_out_list[i] = message_in_list[i]
            
#     return ''.join(char for char in message_out_list)
            
# def decode_word(message_in,shift_distance):    
#     vocab_lexicon = vocabulary[26-shift_distance:] + vocabulary[:26-shift_distance]
#     encode_cipher = dict(zip(vocabulary,vocab_lexicon))
#     message_in_list = list(message_in)
#     message_out_list = ['-']*len(message_in_list)
#     for i in range(0,len(message_in_list)):
#         if message_in_list[i] in vocabulary:
#             message_out_list[i] = encode_cipher[message_in_list[i]]
#         else:
#             message_out_list[i] = message_in_list[i]
            
#     return ''.join(char for char in message_out_list)

def use_cipher(direction,message_in,shift_distance):    
    if direction == 'encode':
        vocab_lexicon = vocabulary[shift_distance:] + vocabulary[:shift_distance]
    else:
        vocab_lexicon = vocabulary[len(vocabulary)-shift_distance:] + vocabulary[:len(vocabulary)-shift_distance]
    encode_cipher = dict(zip(vocabulary,vocab_lexicon))
    message_in_list = list(message_in)
    message_out_list = ['-']*len(message_in_list)
    for i in range(0,len(message_in_list)):
        if message_in_list[i] in vocabulary:
            message_out_list[i] = encode_cipher[message_in_list[i]]
        else:
            message_out_list[i] = message_in_list[i]
            
    return ''.join(char for char in message_out_list)

def run_cipher():    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode','decode']:
        direction = input("You entered an invalid value. Please choose 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    message_in = input("Type your message:\n").lower()
    
    if direction == 'encode':
        shift_distance = int(input("How far would you like your cipher shifted:\n")) % 26
        print("The text {} is encoded as: {}".format(message_in,use_cipher(direction,message_in,shift_distance)))
        restart = input("Would you like to restart the cipher program? (yes or no)\n").lower()
        if restart == 'yes':
            run_cipher()
        else:
            pass
    elif direction == 'decode':
        shift_distance = int(input("How far was your encoding cipher shifted?:\n")) % 26
        print("\nDecoding {} with your original cipher gives: {}".format(message_in,use_cipher(direction,message_in,shift_distance)))
        restart = input("Would you like to restart the cipher program? (yes or no)\n")
        if restart == 'yes':
            run_cipher()
        else:
            pass            
    else:
        print('Tou have not chosen a valid option.')
        restart = input("Would you like to restart the cipher program? (yes or no)\n")
        if restart == 'yes':
            run_cipher()
        else:
            print("Thanks for playing!")
        
run_cipher()




    
    