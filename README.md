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
