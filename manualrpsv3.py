
#This is the main document for the manual RPS game

import random

class RPS():

    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.user_wins = 0
        self.comp_wins = 0
        self.tie = 0
        self.plays = 0

    def get_computer_choice(self):
        compchoice = random.choice(self.options)
        print('The computer picks', compchoice)
        return compchoice

    def get_user_choice(self):
        userchoice = input('You choose: ').lower()
        return userchoice
        

    def find_winner(self, compchoice, userchoice): 
        self.plays += 1

        if userchoice not in self.options:
            print('Your input is invalid')
        
        elif compchoice == userchoice:
            self.tie += 1
            print('It is a draw')
        
        elif self.options.index(userchoice) - self.options.index(compchoice) == -2:
            self.user_wins += 1
            print('You won')

        elif self.options.index(userchoice) - self.options.index(compchoice) == 1:
            self.user_wins += 1
            print('You won')
#above two elif statements have been worked out as the winning subtractions for the option indexes where rock=[0] paper=[1] scissors=[2]
#r-s=-2, p-r & s-p=-1
        else:
            self.comp_wins += 1
            print('You lost')
        
        print('You currently have:', self.user_wins, 'wins and', self.comp_wins, 'losses and', self.tie, 'draws')
        pass

def play_game():
    game = RPS()
    while game.user_wins < 3 or game.comp_wins < 3:
        human_choice = game.get_user_choice()
        computer_choice = game.get_computer_choice()
        game.find_winner(computer_choice, human_choice)
   
        if game.user_wins == 3:
            print("You have won the best of 3")
            exit() 
            
        elif game.comp_wins == 3:
            print("You have lost the best of 3")
            exit() 


#if __name__ == '_main_':
play_game()
