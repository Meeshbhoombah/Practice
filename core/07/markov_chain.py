# -*- encoding: utf-8 -*-
"""
markov_chain.py

This module creates a Markov Chain of given a text file.
"""
import re

class Markov:
    
    def __init__(self, file_name):
        self.words  = self.clean(file_name)


    def clean(self, file_name):
        """ Clean a file object and return it as a list of words """
        with open(file_name, 'r') as f:
            words = f.read()

        words = re.split('[ ,:;?!\n]', words)
        words[:] = [item for item in words if item != '']
        self.tokens = len(words)

        return words


    def chain(self):
        """ Create Markov chain of all words in a file """
        words = list(set(self.words)) # all unique words
   
        chain = {}
        for word in words:
            collection = self.next_word_collection(word)
            chain[word] = self.frequency(collection)
        
        return chain

    def next_word_collection(self, key_word):
        """ A list of all words coming after a given word """
        words = self.words
       
        next_word_indexes = [i + 1 for i, x in enumerate(words) if x == key_word] # get indexes
        next_word_indexes[:] = [i for i in next_word_indexes if i < len(words)] # remove indexes
        collection = [words[index] for index in next_word_indexes] 

        return collection


    def frequency(self, words):
        """ Find the frequency of each word in a list """
        frequency = []
        for word in words:
            frequency.append(words.count(word))

        frequency = list(set(zip(words, frequency)))
        frequency[:] = [(word, (word_frequency / len(words))) for word, word_frequency in frequency]
        frequency = dict(frequency)

        return frequency

if __name__ == "__main__":
    markov = Markov('ganja.txt')
    print(markov.chain())

