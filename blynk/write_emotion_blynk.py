import BlynkLib
from time import sleep
import os

# Change the working directory to where emotion_recognition_all_features.py is
os.chdir('../')

BLYNK_AUTH = 'Hm703ShkXO-pmualjhD1E6xaWBoDwjDH'
# Initialise Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register V0_pin_write_handler for virtual pin V0 write event
@blynk.on("V0")
def V0_pin_write_handler(value):
    buttonValue = value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue == "1":
        print("Starting emotion_recognition_all_features.py")
        
    else:
        print("Stopping emotion_recognition_all_features.py...")

# infinite loop that waits for event
while True:
    blynk.run()
    sleep(.5)
