'''
Created on 14/09/22 @22:09:46  

Finalised version of the camera RPS code
'''

import cv2
from keras.models import load_model
import numpy as np
import random
import time


class RPS():
    ''' A rock paper scissors class where the user is using a trained model and their device camera to input their options. 
    The user mimics the shapes of a rock, paper and scissors that they would use in a real life game and the trained model has learned what these look like
    and can recognise them and use them as the inputted options. As in the manual version of RPS, the computer still picks its options from a list of choices
    '''

    def __init__(self):
        self.options = ['Rock', 'Paper', 'Scissors', 'Nothing']
        self.user_wins = 0
        self.comp_wins = 0
        self.tie = 0
        self.plays = 0
        self.compchoice = []
        self.userchoice = []
        self.model = load_model('keras_model.h5') #Loads the trained model
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    def get_computer_choice(self):
        compchoice = random.choice(self.options[:-1])
        print('The computer picks', compchoice)
        return compchoice
    
    def countdown_timer(self):
        
        time_left = 5
        while time_left > 0:
            print('Image will be captured in', str(time_left), 'seconds')
            cv2.waitKey(1000)
            time_left -= 1
        print('Capturing Image')


    def get_prediction(self):
        '''
        This is where the user makes their choice. They pick either rock, paper or scissors using their hand and this is what is 
        selected as the user option. They also have to do this within a time constraint as shown in both the previous function 
        and the time.time < end_time here. The prediction comes from the factor of it estimating the highest probability of what 
        the user selected and the option returned as a string
        '''
        end_time = time.time() + 5
        while time.time() < end_time:
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            arr = np.argmax(prediction[0])
            user_choice = self.options[arr]
            print(user_choice)
        
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            

        return user_choice
        
    def find_winner(self, compchoice, userchoice): 
        self.plays += 1 #adds one to the game tally

        if userchoice not in self.options:
            print('Your input is invalid') #determines if the users option is one that was in the list

        elif self.options.index(userchoice) == 3:
            print('You did not display an symbol')  #determines if the user even showed a corresponding symbol at all
        
        elif compchoice == userchoice:
            self.tie += 1
            print('It is a draw') #first checks to see if there is a tie
        
        elif self.options.index(userchoice,0,-1) - self.options.index(compchoice,0,-1) == -2:
            self.user_wins += 1
            print('You won')

        elif self.options.index(userchoice,0,-1) - self.options.index(compchoice,0,-1) == 1:
            self.user_wins += 1
            print('You won')
#above two elif statements have been worked out as the winning subtractions for the option indexes where rock=[0] paper=[1] scissors=[2]
#r-s=-2, p-r & s-p=-1
#above lif statements will only run for options that are rock, paper & scissors
        else:
            self.comp_wins += 1
            print('You lost') #only other option is a loss
        
        print('You currently have:', self.user_wins, 'wins and', self.comp_wins, 'losses and', self.tie, 'draws')
        pass

def play_game():
    game = RPS()
    while game.user_wins < 3 or game.comp_wins < 3:
        game.countdown_timer()
        human_choice = game.get_prediction()
        computer_choice = game.get_computer_choice()
        game.find_winner(computer_choice, human_choice)
   
        if game.user_wins == 3:
            print("You have won the first to 3")
            exit() 
            
        elif game.comp_wins == 3:
            print("You have lost the first to 3")
            exit() 

# After the loop release the cap object
    game.cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


#if __name__ == '_main_':
play_game()
