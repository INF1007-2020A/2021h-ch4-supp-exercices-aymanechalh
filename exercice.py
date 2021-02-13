#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
    if len(string)%2==0:
        parity='pair'
    else:
        parity='imapir'



def get_num_char(string, char):
    a=0
    for i in string:
        if i==char:
            a+=1
    return a




def get_first_part_of_name(name):
    b=name.split("-")
    c=b[0]
    e=c.capitalize()
    print(f" Bonjour {e} ")
    return e
def get_random_sentence(animals, adjectives, fruits):
    import random
    a= random.choice(animals)
    b=random.choice(adjectives)
    c=random.choice(fruits)
    return 'Aujourd"hui, j’ai vu un %s s’emparer d’un panier %s plein de %s' %(a,b,c)

if __name__ == "__main__":
    spam = "Bonjour!"
    parity = "pair" if is_even_len(spam) else "impair"
    print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

    eggs = "Hello, world!"
    print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

    parrot = "jean-marc"
    print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

    animals = ("chevreuil", "chien", "pigeon")
    adjectives = ("rouge", "officiel", "lourd")
    fruits = ("pommes", "kiwis", "bananes")
    print(get_random_sentence(animals, adjectives, fruits))
