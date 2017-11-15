# -*- encoding: utf-8 -*-
"""
generate_sentence.py

Create a sentence given a file and the length of the sentence
"""
from markov_chain import Markov
import random

class Process:

    def __init__(self, file_name):
        markov = Markov(file_name)
        self.markov_chain = markov.chain()
        self.unique_words = list(self.markov_chain)


    def create_sentence(self, length):
        """ Creates a sentence given a length """
        sentence = [random.choice(self.unique_words)]
        
        counter = 1
        while (counter < length):
            self.add_word(sentence)
            counter += 1

        return sentence


    def add_word(self, sentence):
        """ Add a new word to the sentence """
        last_word = sentence[-1]
        choices = self.markov_chain[last_word]

        values = list(choices.values())
        keys = list(choices.keys())
        
        if (len(values) > 1) and (len(set(values)) <= 1):
            # random value
            choice = random.choice(keys)
        else:
            choice = max(choices)

        return sentence.append(choice)


if __name__ == "__main__":
    corpus = Process('ganja.txt')
    print(corpus.create_sentence(10))

