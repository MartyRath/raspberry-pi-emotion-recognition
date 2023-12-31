from time import sleep
import os
from blynk_setup import blynk, run_blynk

# register handler for virtual pin V0 write event
@blynk.on("V0")
def write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
        print("Starting...")
        os.system("python3 emotion_recognition_blynk.py")
    else:
        print("Stopping emotion_recognition.py...")
        os.system("pkill -f 'python3 emotion_recognition_blynk.py'")

# infinite loop that waits for event
while True:
    run_blynk()
    sleep(.5)