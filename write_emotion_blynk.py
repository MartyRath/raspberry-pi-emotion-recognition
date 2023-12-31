import BlynkLib
from time import sleep
import subprocess

BLYNK_AUTH = 'Hm703ShkXO-pmualjhD1E6xaWBoDwjDH'
# Initialise Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Process variable to store the running subprocess
current_process = None

# Function to start the script
def start_script():
    global current_process
    if current_process is None or current_process.poll() is not None:
        print("Starting emotion_recognition_all_features.py")
        current_process = subprocess.Popen(['python3', 'emotion_recognition_all_features.py'])

# Function to stop the script
def stop_script():
    global current_process
    if current_process is not None and current_process.poll() is None:
        print("Stopping emotion_recognition_all_features.py...")
        current_process.terminate()

# Register V0_pin_write_handler for virtual pin V0 write event
@blynk.on("V0")
def V0_pin_write_handler(value):
    buttonValue = value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue == "1":
        start_script()
    else:
        stop_script()

# infinite loop that waits for event
while True:
    blynk.run()
    sleep(.5)
