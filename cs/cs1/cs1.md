# Computer Science 1: Programming Fundamentals
Table of Contents
- Roulette.py

## Roulette.py
First, I had to modify

## Hangman.py
**Promp:**
1. Pick a secret word
2. Give a hint: _ _ _ _ _ _ _ _ 
3. Take user guess
    - If guess in word replace it on the
      command line
    - If guess is not in the word
      then add a "body part" to the hangman
4. Display letters guessed
    - Do not allow multiple guesses

**Bonus:**
1. Scrape the Make School website to create a 
   word 

**Writing hangman.py**
Originally, I had created a `Game` class and
intalized it with all the necessary members:
    - a `string` of the secret word
    - a `list` of letters in secret word
    - a `list` of the dashes

But I realized that it was not necessary because
I would not be able to initlaize the class with
any parameters. As a result, I decided to put all
the functions in their own namespace and to use the
keyword global (gasp) to access the variables.

