# -*- encoding: utf-8 -*- #
""" stochastic_sampling.py

This module takes in a file (ganja.txt) and returns the weighted frquencies of each unique word in
that file.

Example:
    Running stocastic_sampling.py creates a log file with the weighted frequencies of each word as
    well as outputs a random word and the weighted frequencies to the CLI.
        $ python3 stochastic_sampling.py
        >>> 'marijuana'
        >>> [('spitting', 0.0013280212483399733), ('dilemma:', 0.0013280212483399733), 
            ('were', 0.0013280212483399733) ... ]

Attributes:

"""
from random import randrange
from decimal import *

with open('gangja.txt', 'r') as f:
    words = f.read()

words = words.split()

def rand_word():
    """ 
    """
    random_word_index = randrange(0, len(words))
    random_word = words[random_word_index]
    
    return random_word


def weighted_frequency():
    """ Find the weighted frequency of repeated words from a source

    Args:
        source_text (list): a list of strings

    Returns:
        histogram (list): a list of of each unique word and the number of times they
            occur in the source_text
    """
    frequency = []
    for word in words:
        frequency.append(words.count(word))
       
    frequency = list(zip(words, frequency))
    frequency = set(frequency)
   
    weighted = []
    for i in range(len(frequency)):
        weighted = [(word, (word_frequency / len(words))) for word, word_frequency in frequency]
        
    print(frequency)
    return weighted

def log():
    weighted = weighted_frequency()
    f = open('weighted_frequencies.txt', 'w')

    for i in range(len(weighted)):
        word = weighted[i][0]
        word_frequency = weighted[i][1]
        word_frequency = str(word_frequency)

        f.write(word + ': frequency = ' + word_frequency + '\n')
            

if __name__ == "__main__":
    """ RANDOM WORD """
    print(rand_word())

    """ WEIGHTED FREQUENCY """
    print(weighted_frequency())

