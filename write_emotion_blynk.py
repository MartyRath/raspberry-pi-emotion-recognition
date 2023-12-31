from time import sleep
import os
from blynk_setup import blynk, run_blynk

# flag to control the execution of emotion_recognition_blynk.py
emotion_recognition_running = False

# register handler for virtual pin V0 write event
@blynk.on("V0")
def write_handler(value):
    global emotion_recognition_running
    buttonValue = value[0]
    print(f'Current button value: {buttonValue}')
    
    if buttonValue == "1":
        if not emotion_recognition_running:
            print("Starting emotion_recognition_blynk.py...")
            os.system("python3 emotion_recognition_blynk.py &")
            emotion_recognition_running = True
        else:
            print("Emotion recognition already running.")
    else:
        if emotion_recognition_running:
            print("Stopping emotion_recognition_blynk.py...")
            emotion_recognition_running = False
        else:
            print("Emotion recognition already stopped.")

# infinite loop that waits for event
while True:
    run_blynk()
    sleep(.5)
