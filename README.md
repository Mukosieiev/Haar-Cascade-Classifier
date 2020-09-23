# Demonstration
[![YOUTUBE Video](http://img.youtube.com/vi/-lNZPx-Hu2g/0.jpg)](https://www.youtube.com/watch?v=-lNZPx-Hu2g "Video demonstration")
# Haar-Cascade-Classifier
The following project is the demonstration of the deep learning image classifier that is written in Python using OpenCV. 
I supplied the images of my face into the algorithm, and made the machine recognize my face.


### Prerequisites
You would have to install the OpenCV and NumPy. Type in the following in your console:
```
pip3 install cv2
pip3 install numpy
```
### Installation
Download the .py and .XML files and put them in the same directory. Change the route to the .XML classifier (line 20 inside .py file) on your computer and run the application.
## Dataset
For any machine learning algorithm to work, you have to supply the dataset of the positive and negative images. 
### Positive images 
The images that contain my face. This dataset was made on the frontal camera of my iPhone 6 and listed 300+ pictures.
### Negative images 
The images that do not contain my face. 
This dataset had a total of 3,182 images and contained everything from the grass to the planes. 
All pictures were converted to black and white colors in order to decrease the training time for the machine. 
I downloaded all the negative images from the [image-net](http://www.image-net.org/).
## Training
The training process took me a little less than 2 hours. I trained the classifier using the [DigitalOcean](https://www.digitalocean.com/) server.

[![IMAGE ALT TEXT](http://img.youtube.com/vi/-lNZPx-Hu2g/0.jpg)](https://www.youtube.com/watch?v=-lNZPx-Hu2g "Video Title")
