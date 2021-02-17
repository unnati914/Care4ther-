# CARE4THER APP USING ML AND ANDROID 
Nearly 80% of accidents take place yearly. This piece of code will help the users to detect an accident an a early stage and it is detected by different libraries like Deep learning etc.

# Code Requirements
You can install Conda for python which resolves all the dependencies for machine learning.
pip install requirements.txt

# Procedure
Run create_dataset.py for converting the video to images.
Then run main.py to train the model.
Finally, run model.py for testing your model.
The Algorithm:
Each video is a set of individual images that are time-dependent sequences. The algorithm - a hierarchical recurrent neural network - is able to treat each video as a time-dependent sequence, but still allow each video to be an independent data point.

The algorithm uses two layers of long short-term memory neural networks. The first neural network (NN) is a recurrent network that analyzes the time-dependent sequence of the images within each video. The second takes the encoding of the first NN and builds a second NN that reflects which videos contain accidents and which do not. The resulting model enables a prediction of whether new dashcam footage has an accident.

Through this method, the HRNN incorporates a time-dependent aspect of the frames within each video to predict how likely it is a new video contains a car accident.


# *VARIOUS TECHNOLOGIES USED IN THE PROJECT*


1. DEEP LEARNING
2. MACHINE LEARNING
3. ANDROID
4. JAVA
5. CNN

# *Why this project is important*
To prevent accidents , this is the app that can tell the location of the accident and it could prevent the accidents.

# *FEATURES OF THE APP*
The app is made using Java language, various features are being added in the app like.. alert system for an accident,sensors,etc

Try implementing this project and suggest changes:)
Happy Learning!
