'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
random.seed(1)

bet_amount = 0
bet_color = None
bet_number = None

green = [0]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def roll_ball():
    # returns a random number between 0 - 37
    return random.randint(0, 38)

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    bank_account = 1000
    bankrupt = False
 
    roundNumber = 1
    end_game = False

    intro = """
    Welcome to roulette. You have $%s in your bank account.

    Make a bet between $1 and $1000 and select a number between
    0 and 37 to bet on.
    """ % bank_account
    print(intro) 
     
    while(not bankrupt and not end_game):
        switcher = input("Choose between a bet on (C)olor or (N)umber: ")
        
        if switcher == "C" or switcher == "c": 
            bet = int(input("Bet color (green/red/black):  "))
        elif switcher == "N" or switcher == "n":
            bet = int(input("Bet number (0-37): "))
        else:
            print("Please choose either C or N")
            switcher = input("Choose between a bet on (C)olor or (N)umber: ")
        
        amount = int(input("Bet amount (At least 10 with a limit of {}) ".format(bank_account)))
        
        check_results(roll_ball(), bet, amount)
        if winnings > 0:
            print("You made ${}. Congratulations!".format(winnings))
            bank_account = winnings
        else:
            print("You lost ${}. Unfortunate. You lost!".format(winnings))
            bank_account = winnings
        
        next_round = input("You now have ${}. Another round (y/n)? ".format(bank_account))
        if next_round == "y":
            roundNumber += 1
        else:
            end_game = True
            break

    print ("Thanks for playing. You ended with ${} after {} round(s)".format(bank_account, roundNumber))

def check_results(number_rolled, bet, amount):
    # Compares bet_color to color rolled. Compares
    # bet_number to number_rolled. Returns payout for bet.
    
    if (type(bet) is int):
        if bet == number_rolled:
            bank_account  = 2 * amount + bank_account
        else:
            bank_account = bank_account - amount
    else:
        if number_rolled in red:
            if bet == "red":
                bank_account = amount / 2 + bank_account
        elif number_rolled != 0:
            if bet == "black":
                bank_account = amount / 2 + bank_account
        elif bet == "green":
            bank_account = amount / 2 + bank_account
        else:
            bank_account = bank_account - amount

play_game()
