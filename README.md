# raspberry-pi-emotion-recognition
Project Name: The "How's it going?" Hat - Using a Raspberry Pi with camera for emotion recognition

Grade: 86%

**Introduction**

My partner is autistic and often has trouble interpreting emotion. The purpose of this project is to develop a device that can interpret emotion in real-time via a camera and communicate those emotions with the user. The device is aimed at users who have trouble recognising facial expressions. 
![howitworkswithtext](https://github.com/MartyRath/raspberry-pi-emotion-recognition/assets/91559109/6bb6e446-de80-48fb-90ec-e501bee1d25d)

**Result**


See the full video walkthrough here: 
[![Watch the video](https://img.youtube.com/vi/JRKy4CD8RQc/maxresdefault.jpg)](https://www.youtube.com/watch?v=JRKy4CD8RQc)

The device recognises seven emotions which are communicated with the user when an emotion changes via connected Bluetooth device and visually via Blynk app. An image is also stored and processed when an emotion changes to be stored via Firebase to create a dataset to train future models. 

**Technologies Used**

Hardware

•	Processing: Raspberry Pi 4 Model B
•	Sensor: Logitech Web Cam

Programming

•	Device: Windows 10 computer
•	IDE: Visual Studio Code to remotely access Pi via SSH
•	Language: Python, including os and subprocess to work with Linux commands
•	WSL to work on project without Pi
•	Shell scripting and Linux commands

Emotion Recognition

•	Face detection: OpenCV
•	Emotion recognition: TensorFlow Lite

Communication with Pi

•	Blynk app to switch on/on emotion recognition, display detected emotions as emoticons.
•	Bluetooth from Pi to speaker to communicate detected emotions.
•	SSH Secure Shell for headless connection to Pi

Database

•	Firebase to store processed emotion images and emotion labels with timestamp

**References**

DigitalSreeni, 2021 - Main reference video series:

•	Tips Tricks 18 - Extracting faces from images for deep learning training
Video: https://www.youtube.com/watch?v=9T9L9HoUFZ0&list=PL-DybH_1zzKv4yVdGeM04t5OfvJPvqLwv&index=1&pp=gAQBiAQB
GitHub: https://github.com/bnsreenu/python_for_microscopists/blob/master/Tips_tricks_18_Extracting%20faces%20from%20images%20for%20deep%20learning%20model%20training.py

•	237 - What is Tensorflow Lite and how to convert keras model to tflite?
Video: https://www.youtube.com/watch?v=HXzz87WVm6c&list=PL-DybH_1zzKv4yVdGeM04t5OfvJPvqLwv&index=2
GitHub: https://github.com/bnsreenu/python_for_microscopists/tree/master/237_tflite_using_malaria_binary_classification

•	238 - Real time face detection using opencv (and video feed from a webcam)
Video: https://www.youtube.com/watch?v=Fuve1nAdm8k&list=PL-DybH_1zzKv4yVdGeM04t5OfvJPvqLwv&index=3
GitHub: 
https://github.com/bnsreenu/python_for_microscopists/tree/master/238_face_eye_detection_using_opencv

•	Note: Used to train emotion detection model using Kera library, output h5 file: 239 - Deep Learning training for facial emotion detection
Video: https://www.youtube.com/watch?v=P4OevrwTq78&list=PL-DybH_1zzKv4yVdGeM04t5OfvJPvqLwv&index=4&pp=gAQBiAQB
GitHub: https://github.com/bnsreenu/python_for_microscopists/tree/master/239_train_emotion_detection

•	Note: Used for main emotion detection file: 241 - Real time detection of facial emotion, age, and gender (using video feed from a webcam)
Video: https://www.youtube.com/watch?v=JmvmUWIP2v8&list=PL-DybH_1zzKv4yVdGeM04t5OfvJPvqLwv&index=5
GitHub: https://github.com/bnsreenu/python_for_microscopists/tree/master/241_live_age_gender_emotion_detection

•	Note: Used to convert h5 to TensorFlow Lite model: 242 - Real time detection of facial emotion, age, and gender using TensorFlow Lite (on Windows10) 
Video: https://www.youtube.com/watch?v=NJpS-sFGLng&list=PL-DybH_1zzKv4yVdGeM04t5OfvJPvqLwv&index=6
GitHub: https://github.com/bnsreenu/python_for_microscopists/tree/master/242%20-%20Real%20time%20detection%20of%20facial%20emotion%2C%20age%2C%20and%20gender%20using%20TensorFlow%20Lite

•	Note: Used as a guide to instal OpenCV and TensorFlow lite on Raspberry Pi: 243 - Real time detection of facial emotion, age, and gender using TensorFlow Lite on RaspberryPi
Video: https://www.youtube.com/watch?v=j6i4YTFlYRA&list=PL-DybH_1zzKv4yVdGeM04t5OfvJPvqLwv&index=7
GitHub: https://github.com/bnsreenu/python_for_microscopists/tree/master/243%20-%20Real%20time%20detection%20of%20facial%20emotion%2C%20age%2C%20and%20gender%20using%20TensorFlow%20Lite%20on%20RaspberryPi

Open CV Haar Cascade model for face detection:
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

Kaggle Dataset used to train emotion detection model:
https://www.kaggle.com/msambare/fer2013

OpenCV installation on Raspberry Pi (jasper-dev dependency not installed):
https://raspberrypi-guide.github.io/programming/install-opencv

Tflite Runtime Wheel sourced from PyPi.org:
https://pypi.org/project/tflite-runtime/2.14.0/#files

TensorFlow learning aid: TensorFlow in 100 Seconds
https://www.youtube.com/watch?v=i8NETqtGHms

Emoticons used in Blynk:
https://www.flaticon.com/

Relative paths Python, os.path.join
https://stackoverflow.com/questions/918154/relative-paths-in-python

Firebase .exists():
https://stackoverflow.com/questions/37751202/how-to-check-if-file-exists-in-firebase-storage

Firebase blob:
https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob

Crontab for running script on start up:
https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/

PulseAudio issue fix:
https://unix.stackexchange.com/questions/445386/pulseaudio-server-connection-failure-connection-refused-debian-stretch

