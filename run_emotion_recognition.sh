#!/bin/bash

# Redirect output to a log file to debug
exec &>> /home/marty/assignment/raspberry-pi-emotion-recognition/debug.log

# Navigate to the directory
cd /home/marty/assignment/raspberry-pi-emotion-recognition || { echo "Failed to change directory. Exiting."; exit 1; }

# Activate virtual environment
source /home/marty/assignment/raspberry-pi-emotion-recognition/virtualenv/bin/activate || { echo "Failed to activate virtual environment. Exiting."; exit 1; }

# Run emotion detection
python3 01_emotion_recognition_all_features.py
