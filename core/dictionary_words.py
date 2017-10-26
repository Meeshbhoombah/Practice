# -*- encoding: utf-8 -*-
"""
rearrange.py

This scripts reaches into the local dictionary of words, the length of which is specefied by the
user

Attributes:
    words (file object): A file containing the user's local dictionary of words
Example:
    $ python3 dictionary_words.py 3
    >> wuss paragrammatist avitaminosis.
"""

import sys
import random

with open("/usr/share/dict/words", "r") as f:
    words = f.read()

def create_sentence(length):
    """ Creates a sentence given a length

    Args:
        length (int): the length of the string as specefied by the user 

    Returns:
        sentence (str): the generated sentence
    """
    sentence = ""

    for i in range(length):
        lines = words.splitlines()
        line_number = random.randrange(0, len(lines))
        word = lines[line_number]

        if i == length - 1:
            sentence += (word + ".")
        else:
            sentence += (word + " ")

    return sentence


if __name__ == "__main__":
    user_args = sys.argv[1]
    sentence_length = int(user_args)

    sentence = create_sentence(sentence_length)
    print(sentence)

