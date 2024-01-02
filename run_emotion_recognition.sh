#!/bin/bash
# This navigates to emotion recogntion project directory, starts virtual environment
# and then starts emotion recognition.

# Clear log file
> /home/marty/assignment/raspberry-pi-emotion-recognition/debug.log

# Redirect output to a log file to debug
exec &>> /home/marty/assignment/raspberry-pi-emotion-recognition/debug.log

# Fixes issue Connection failure: Connection refused pa_context_connect() failed: Connection refused
pulseaudio --start

device_name="SoundCore 2"

# While bluetoothctl info does not contain "Connected: yes", do...
while ! bluetoothctl info | grep -q "Connected: yes"; do
    # Attempt to connect
    bluetoothctl connect "$device_name"
    sleep 2
done
echo "Bluetooth connected"

echo "Press ON to start emotion recognition"

cd /home/marty/assignment/raspberry-pi-emotion-recognition

virtualenv/bin/python3 01_emotion_recognition_all_features.py