'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
random.seed(1)

game_over = False
end_game = False

bank_account = 1000
bankrupt = False

bet_amount = 0
bet_color = None
bet_number = None

green = [0]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def roll_ball():
    # returns a random number between 0 - 37
    return random.randint(0, 38)

def check_results(number_rolled, color, number, amount):
    # Compares bet_color to color rolled. Compares
    # bet_number to number_rolled. Returns payout for bet.
    if number == number_rolled:
        payout = 2 * amount
    
    if number_rolled in red:
        if color == "red":
            payout == amount / 2
    elif number_rolled != 0:
        if color == "black":
            payout == amount / 2
    elif color == "green":
        payout == amount / 2
    else:
        payout = 0
        
    return payout

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    intro = """
    Welcome to roulette. You have $%s in your bank account.

    Make a bet between $1 and $1000 and select a number between
    0 and 37 to bet on.
    """ % bank_account
    print intro 
    
    while(not bankrupt and not end_game):
        switcher = raw_input("Choose between a bet on (C)olor or (N)umber")
        
        if switcher == "C": 
            bet = raw_input("Bet color (green/red/black):  ")
        else
            bet = int(raw_input("Bet number (0-37): "))
        
        amount = raw_input("Bet amount (At least 10 with a limit of %s") % (bank_account)
        
        results = check_results(roll_ball(), bet, amount)
        
        if results < 0:
            print "You made $" + results ". Congratulations!"
        else:
            print "You lost $" + results ". Unfortunate. You lost!"
        
        next_round = raw_input("You now have %s. Another round (y/n)? ") %s bank_account
        if next_round == "y":
            roundNumber +=
            pass
        else:
            end_game = True
            break

    print "Thanks for playing. You ended with $%s after %s rounds" % (bank_account, roundNumber)

play_game()
