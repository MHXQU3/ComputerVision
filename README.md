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
