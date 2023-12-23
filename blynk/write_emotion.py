import BlynkLib
import random
import time

BLYNK_AUTH = 'Hm703ShkXO-pmualjhD1E6xaWBoDwjDH'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

emotions = [1,2,3,4,5,6,7]

while True:
    random_emotion = random.choice(emotions)
    print(random_emotion)
    blynk.run()
    blynk.virtual_write(1, random_emotion)
    time.sleep(.5)