# -*- encoding: utf-8 -*-
"""
histogram.py

Histogram can find the frequency or weighted frequency of words in a file, both of which can be
returned as either a list or a dictionary. Histogram can also return a random word from a given
corpus.
"""
from random import randrange
import re

class Histogram:

    def __init__(self, file_name = None, list_type = 0):
        """ Initalize the histogram dict """
        self.words      = self.clean(file_name)
        self.types      = 0  # Number of distinct words
        self.tokens     = 0  # Total count of all words
        self.list_type  = list_type

    
    def clean(self, file_name):
        """ Clean a file object and return it as a list of words """
        with open(file_name, 'r') as f:
            words = f.read()

        words = re.split('[, ?!-.\n]', words) # TODO - fix splitting on ' (ex. it's -> it s)
        self.tokens = len(words)

        return words


    def random_word(self, words = None):
        """ Get a random word """
        if words is None:
            words = self.words

        index = randrange(0, len(words))
        word = words[index]
        return word


    def frequency(self, words = None):
        """ Find the frequency of each word in the corpus """
        if words is None:
            words = self.words
        
        frequency = []
        for word in words:
            frequency.append(words.count(word))

        frequency = list(set(zip(words, frequency)))
        self.types = len(frequency) # Frequency only contains unique words
        
        if self.list_type == 1:
            return dict(frequency)

        return frequency


    def weighted_frequency(self, words = None, frequency = None):
        """ Find the weighted frequency of each word in the corpus """
        if words is None:
            words = self.words
        if frequency is None:
            frequency = self.frequency()

        if type(frequency) is dict:
            frequency = frequency.items()

        weighted = []
        for i in range(self.types):
            weighted = [(word, (word_frequency / len(words))) for word, word_frequency in frequency]
        
        if self.list_type == 1:
            return dict(weighted)

        return weighted


if __name__ == '__main__':
    import sys
    file_name = str(sys.argv[1])

    if len(sys.argv) >= 3:
        output_type = int(sys.argv[2])
    else:
        output_type = 0

    histogram = Histogram(file_name, output_type) # 0 for list, 1 for dict
        
