import BlynkLib
from time import sleep
import os

# Change the working directory to where emotion_recognition.py is
os.chdir('../')

BLYNK_AUTH = 'Hm703ShkXO-pmualjhD1E6xaWBoDwjDH'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# register handler for virtual pin V0 write event
@blynk.on("V0")
def v3_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
        print("Starting emotion_recognition_all_features.py")
        os.system("python3 emotion_recognition_all_features.py &")
    else:
        print("Stopping emotion_recognition_all_features.py...")
        os.system("pkill -f 'python3 emotion_recognition_all_features.py'")

# infinite loop that waits for event
while True:
    blynk.run()
    sleep(.5)