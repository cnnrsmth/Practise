#DEFs

#import relevant modules
import random

#global variable
values = {0: 'green', 1: 'red', 3: 'red', 5: 'red', 7: 'red', 9: 'red', 12: 'red', 14: 'red', 16: 'red', 18: 'red', 19: 'red', 21: 'red', 23: 'red', 25: 'red', 27: 'red', 30: 'red', 32: 'red', 34: 'red', 36: 'red', 2: 'black', 4: 'black', 6: 'black', 8: 'black', 10: 'black', 11: 'black', 13: 'black', 15: 'black', 17: 'black', 20: 'black', 22: 'black', 24: 'black', 26: 'black', 28: 'black', 29: 'black', 31: 'black', 33: 'black', 35: 'black'}

#class to track gains and losses (eliminating overuse of global variables)
class Bankroll():
    
    def __init__(self):
        self.total = 1000
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


#function to take qty stake

def take_stake(bankroll):
    
    bankroll.bet = int(input(f'How much money would you like to bet? You have £{bankroll.total}'))


#function to take bet 

def take_bet():

    bet = (input("What colour would you like to pick? Enter red or black" ))

    if bet[0].lower() == 'r' or bet[0].lower() == 'b':
        return bet
    else:
        print("Incorrect input")


#function to spin the wheel

def spin():
    spin_outcome = random.randint(0,36)
    return spin_outcome

#function to check colour of number that ball landed on

def colour_check(spin_outcome):
    
    global values
    
    for number,colour in values.items():
        if spin_outcome == number:
            return colour
        else:
            continue

#function to check if user's bet hit the colour

def win_check(colour_check,bet,bankroll):

    if colour_check == bet:
        bankroll.win_bet()
        print("You've won")
    
    else:
        bankroll.lose_bet()
        print("You've lost")
        return False

#function to print the outcome

def print_outcome(spin_outcome,colour):

    print(f"The roulette spin landed on {spin_outcome} {colour}")


#GAMEPLAY

#set up the players bank

player_bank = Bankroll()

Playing = True

while Playing:  

    #ask for player stake

    take_stake(player_bank)

    #ask for player bet

    player_bet = take_bet()

    #spin the wheel

    spin_result = spin()

    #check the colour

    spin_colour = colour_check(spin_result)

    #check if player wins

    player_outcome = win_check(spin_colour,player_bet,player_bank)

    #return the outcome

    print_outcome(spin_result, spin_colour)

    #ask to play again

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        Playing = True
    else:
        print("Thanks for playing!")
        Playing = False