import os
import sys
import random
import time

start_time = time.time()
with open("/usr/share/dict/words", "r") as directory:
    file_content = directory.read()

num = 10

def randomize(num):
    string_list = file_content.split("\n")
    word_list = random.choice(string_list)
    randomize = " ".join(random.choice(string_list) for i in range(num))
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    return randomize

randomize(num)
