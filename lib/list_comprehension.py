#!/usr/bin/env python3

def return_evens(num_list):
    even_elements = []
    for num in num_list:
        if num % 2 == 0:
            even_elements.append(num)
    return even_elements
    

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]
    