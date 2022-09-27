# ComputerVision
 Repo for the AI Core computer vision project

## Preparation

- This milestone required the use of teachable machine. An online tool that creates a machine learning model based on images, audio or bodily poses. In this case we used the image option. This required us to create several classes for each symbol and register numerous images to each class so the AI can learn to recognise whenever each of these symbols are shown. Multiple versions of these images were input into the machine, e.g. images with the face and body in frame, images without face and body in frame and images where the symbol were shown in different orientations.
- The model was then downloaded as a keras model file. This option was picked due to keras being an API that is tightly integrated with TensorFlow which is a software library which focuses on training deep neural networks
- Tensorflow is one of the packages that were downloaded in the conda environment. Opencv-python (opencv-python headless was one I also downloaded) and ipykernel.
- OpenCV is used for computer vision projects as it helps with image processing via the camera etc and ipykernel is the package for the Jupyter notebook.

## Manual RPS Game

- This section is regarding the code that played a manually operated RPS game. Manual being one where the user types their input as to which of the 3 options they will pick.

### Defining the initialiser

- The initialiser for this project consisted of defining the list of options and the various score variables such as win, loss, draw and how many games have been played.

```python
def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.user_wins = 0
        self.comp_wins = 0
        self.tie = 0
        self.plays = 0
```

### Defining both the choices

- This section will focus on the code which defined both the computer and user choices.

#### Defining the computer choice

- The computer choice was defined as a random choice from the list of 3 options which was defined in the initialiser. A statement was printed which displayed the computers choice in the game. The choice was then returned to close out the class.

```python
def get_computer_choice(self):
        compchoice = random.choice(self.options)
        print('The computer picks', compchoice)
        return compchoice
```

#### Defining the user choice

- The user choice made use of the input function. The .lower() function was then used to ensure the input was converted into entirely lowercase regardless of what case the original input was. This was done as lowercase seemed the most friendly case for inputs, so the list was made all lowercase too. Again, this variable was returned to close out the class.

```python
def get_user_choice(self):
        userchoice = input('You choose: ').lower()
        return userchoice
```    

### Finding the winner

- This part of the code is where the winner is found every match. The first part of the code is checking for a valid input. If the input is not in the list of options then the input is not taken and an input is asked for again. Index calculation is utilised to work out who the winner is. Based on the indexes in the list {rock,paper,scissors}, rock is 0, paper is 1 and scissors is 2. rock beats scissors, so the calculation would be 0-2 = -2, paper beats rock and scissors beats paper which gives the calculations of 1-0 and 2-1, both of which result in 1. These calculations are done with the user input being the first variable in the calculation, so if -2 or 1 was the output of the calculation, the user wins, the win counter is increased by 1 and a statement would be displayed showing so. if the user input is equal to the computer input then the game would result in a draw, the draw counter is increased by 1 and a statement would be printed showing so and if neither of these conditions are ment then the only other outcome possible would be that the user has lost the game in which case the loss counter is increased by 1 and a statement is displayed showing the user has lost. 

```python
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
```
