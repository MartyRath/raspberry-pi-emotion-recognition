#!/bin/bash
# This navigates to emotion recogntion project directory, starts virtual environment
# and then starts emotion recognition.

# Clear log file
> /home/marty/assignment/raspberry-pi-emotion-recognition/debug.log


# Redirect output to a log file to debug
exec &>> /home/marty/assignment/raspberry-pi-emotion-recognition/debug.log

device_name="Jabra Elite Active 75t"

# While bluetoothctl info does not contain "Connected: yes", do...
while ! bluetoothctl info | grep -q "Connected: yes"; do
    # Attempt to connect
    bluetoothctl connect "$device_name"
    sleep 2
done
echo "Bluetooth connected"

# gets bluetooth audio sink index from list
bluetooth_index=$(pactl list short sinks | grep "bluez" | awk '{print $1}')
# Sets default audio sink by index from list
pactl set-default-sink $bluetooth_index

# Redirect output to a log file to debug
exec &>> /home/marty/assignment/raspberry-pi-emotion-recognition/debug.log

cd /home/marty/assignment/raspberry-pi-emotion-recognition

virtualenv/bin/python3 01_emotion_recognition_all_features.py