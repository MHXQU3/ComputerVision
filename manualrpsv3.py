
#This is the main document for the manual RPS game

import random

class RPS():

    def __init__(self):
        self.options = ['rock', 'paper', 'scissors'] #The standard rock paper scissors options
        self.user_wins = 0 #No. of user wins
        self.comp_wins = 0 #No. of computer wins
        self.tie = 0 #No. of draws
        self.plays = 0 #No. of games played

    def get_computer_choice(self):
        compchoice = random.choice(self.options) #This function provides a random choice from the options in self.options
        print('The computer picks', compchoice)  #Statement displaying what the computer has selected
        return compchoice

    def get_user_choice(self):
        userchoice = str(input('You choose: ')).lower() #Asks the user for an input
        if userchoice not in self.options: #Checks the input is in the options list
            print("Please select a valid option")
        else:
            return userchoice #If the input passes the check, then the input will be returned
        

    def find_winner(self, compchoice, userchoice):  # Function passes the computer and user choice as arguments 
        self.plays += 1 #Adds one to the game tally

        if compchoice == userchoice: #Checks to see if the outcome is a draw first
            self.tie += 1 #Adds one to the draw coutner
            print('It is a draw')
        
        elif self.options.index(userchoice) - self.options.index(compchoice) == -2: #Uses indexes to see if the user has beaten the computer
            self.user_wins += 1
            print('You won')

        elif self.options.index(userchoice) - self.options.index(compchoice) == 1: #Uses indexes to see if the user has beaten the computer
            self.user_wins += 1
            print('You won')
#above two elif statements have been worked out as the winning subtractions for the option indexes where rock=[0] paper=[1] scissors=[2]
#r-s=-2, p-r & s-p=-1
        else:
            self.comp_wins += 1 #Only other outcome is a loss hence the else statement
            print('You lost')
        
        print('You currently have:', self.user_wins, 'wins and', self.comp_wins, 'losses and', self.tie, 'draws')
        pass

def play_game():
    game = RPS()
    while game.user_wins < 3 or game.comp_wins < 3: #Code for a first to 3 game, number can be altered to increase no. of games
        human_choice = game.get_user_choice()
        computer_choice = game.get_computer_choice()
        game.find_winner(computer_choice, human_choice)
   
        if game.user_wins == 3:
            print("You have won the first to 3")
            exit() 
            
        elif game.comp_wins == 3:
            print("You have lost the first to 3")
            exit() 


#if __name__ == '_main_':
play_game()
