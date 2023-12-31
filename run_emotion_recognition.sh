#!/bin/bash

cd /home/marty/assignment/raspberry-pi-emotion-recognition

# Activate virtual environment
source /home/marty/assignment/raspberry-pi-emotion-recognition/virtualenv/bin/activate

# Run emotion detection
python3 01_emotion_recognition_all_features.py
