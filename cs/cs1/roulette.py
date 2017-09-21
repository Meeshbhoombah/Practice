import random
import re

bank_acount = 1000
bet = {
    "type": "none",
    "amount": 0,
    "number": 0
}

color = {
    "green": [0, 37],
    "red": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
    "black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
}

intro = True

bankrupt = False
end_game = False
rounds = 1

print('''
     _ __           _           
    ( /  )         //   _/__/_  
     /--<  __ , , // _  /  /  _ 
    /   \_(_)(_/_(/_(/_(__(__(/_
                                   
    (P)lay the Game *OR* (L)earn the rules

    ''')

while(intro):
    user_action = input()
    menuOption(user_action)

def menuOption(option):
    if user_action == "P" or "p":
        intro = False
        play_game()
    elif user_action == "L" or "l":
        intro = False
        rules()
    else:
        print("Please enter (P) or (L)")

def rules():
    learned = False
        
    while not learned:
        print('''
        
        Bets you can make:
        - Odd, Even, Black, Red (1:1 payout)
        - A single number (0 - 36 and 00)

        Simple, right?
        ''')
    
        game = input("Type continue to start game ")
        if game.lower() == "continue":
            learned = True
        else:
            pass

def play_game():
    while not bankrupt and not end_game:

        bet_set = False
        while not bet_set:
            user_bet = input("Place your bet: ")
            if  validateBet(user_input):
                bet_set = True
            else:
                print("Not a valid bet.")
                pass
        
        wager_set = False
        while not wager_set:
            user_wager = input("Place your wager: ")
            if validateWager(user_wager):     
                wager_set = True
            else:
                print("Not a valid wager.")
                pass

        house_roll = rollBall()
        won = checkBet(house_roll)

        if won == True:
            userWon(bet, bank_account)
        else:
            userLost(bet, bank_account)

        if bankrupt == True:
            break
            
        another_round = input("Do you want to play another round? (Y/N) ")
        if another_round == "Y" or "y":
            rounds += 1
            pass
        else:
            end_game = True
            break

    if not bankrupt:
        print("Thanks for playing! After {} rounds you ended with ${}".format(rounds, bank_account))
    else:
        print("You ran outta money! We're comin' for ya. Good luck on the streets.")

def validateBet(bet):
    if bet.lower() == "odd" or "even" or "black" or "red":
        bet["type"] == bet
        return True
    elif bet == "00":
        bet["type"] = "single number"
        bet["number"] = 37
    elif any(char.isdigit() for char in bet):
        bet["type"] == "single number"
        bet["number"] == int(bet)
        return True
    else:
        return False
    
def validateWager(wager):
    try:
        int(wage)
        return True
    except ValueError:
        return False
           
def rollBall():
    random.seed(1)
    return random.randint(0, 38)

def checkBet(roll):
    if bet["number"] != 0 and bet == roll:
        return True
        bet["amount"] = bet["amount"] * 35
    elif isinstance(bet, str):
        if bet["type"] == "odd" and roll % 2 != 0:
            return True
        elif bet["type"] == "even" and roll % 2 == 0:
            return True
        elif bet["type"] == "red" and roll in color["red"]:
            return True
        elif bet["type"] == "black" and roll in color["black"]:
            return True
        elif bet["type"] == "single number" and roll == 37:
            return True
            bet["amount"] =  bet["amount"] * 35
    else:
        return False

def userWon(user_bet, user_bank_account):
    user_bank_account = bet["amount"] + user_bank_account
    print("Nice win! Your bank account is now at ${}".format(user_bank_account))

def userLost(user_bet, user_bank_account):
    user_bank_account = user_bank_account - bet["amount"]
    print("You lost! Your bank account is now at ${}".format(user_bank_account))

