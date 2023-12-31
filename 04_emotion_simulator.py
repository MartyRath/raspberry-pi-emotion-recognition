import random
import time

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

while True:
    random_emotion = random.choice(emotions)
    print(random_emotion)
    time.sleep(5)  # Wait for 5 seconds before generating the next emotion