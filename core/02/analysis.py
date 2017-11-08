# -*- encoding: utf-8 -*-
""" analysis.py

Takes a source_text (which has been read in and broken down into a list of words) and
can output a histogram of the frequency of word occurance, all the unique words in
the text, or the number of times a singular word appears in the source text.
"""
import re

class Analyzer:
    
    def __init___(self):
        pass    
    
    def histogram(self, source_text):
        """ Find the frequency of repeated words from a source

        Args:
            source_text (list): a list of strings

        Returns:
            histogram (list): a list of of each unique word and the number of times they
                occur in the source_text
        """
        source = source_text
        histogram = []

        for word in source: 
            histogram.append(source.count(word))

        histogram = list(zip(source, histogram))
        histogram = set(histogram)
        return histogram 


    def unique_words(self, histogram):
        """ Find all unique words in source text

        Args:
            histogram (list): a list of tuples containing each word and it's frequency

        Returns:
            unique_words (list): a list of all the unique words from the source
        """
        unique_words = [(word) for word, frequency in histogram]
        return unique_words
    

    def frequency(self, word, histogram):
        """ Find the frequency of a single word

        Args:
            word (str): the word of which the frequency will be returned
            histogram (list): a list of tuples containing each word and it's frequency

        Returns:
            frequency (int): the number of times the given word occurs in the source text
                as parsed from the histogram
        """
        histogram = dict(histogram)
        frequency = histogram[word]

        return frequency
 
    
if __name__ == "__main__":
    """ MODULE SET UP """
    analyzer = Analyzer()
    with open('gangja.txt', 'r') as f:
        words = f.read()
    
    words = words.split()
    #words = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
    
    """ HISTOGRAM """
    histogram = analyzer.histogram(words)
    print("Histogram: " + str(histogram))

    """ UNIQUE WORDS """
    unique_words = analyzer.unique_words(histogram)
    print("Unique words: " + str(unique_words))

    """ FREQUENCY """
    #word = "fish"
    word = "gangja"
    frequency = analyzer.frequency(word, histogram)
    frequency = str(frequency)
    print("Frequency of " + word + ": " + frequency)

