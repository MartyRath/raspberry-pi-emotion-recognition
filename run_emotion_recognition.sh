#!/bin/sh
# This navigates to emotion recogntion project directory, starts virtual environment
# and then starts emotion recognition.

cd /home/marty/assignment/raspberry-pi-emotion-recognition
exec &>> /home/marty/assignment/raspberry-pi-emotion-recognition/debug.log
/home/marty/assignment/raspberry-pi-emotion-recognition/virtualenv/bin/python3 01_emotion_recognition_all_features.py