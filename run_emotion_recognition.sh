#!/bin/sh
# This navigates to emotion recogntion project directory, starts virtual environment
# and then starts emotion recognition.

DEVICE_NAME="Jabra Elite Active 75t"

# While bluetoothctl info does not contain "Connected: yes", do...
while ! bluetoothctl info | grep -q "Connected: yes"; do
    # Attempt to connect
    bluetoothctl connect "$DEVICE_NAME"
    sleep 2
done
echo "Bluetooth connected"

cd /home/marty/assignment/raspberry-pi-emotion-recognition

virtualenv/bin/python3 01_emotion_recognition_all_features.py