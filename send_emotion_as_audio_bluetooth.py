import random
import time
from playsound import playsound
import os

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Dictionary mapping emotions to audio file names or paths
emotion_audio = {
    'Angry': os.path.join('audio', 'angry.mp3'),
    'Disgust': os.path.join('audio', 'disgust.mp3'),
    'Fear': os.path.join('audio', 'fear.mp3'),
    'Happy': os.path.join('audio', 'happy.mp3'),
    'Neutral': os.path.join('audio', 'sad.mp3'),
    'Sad': os.path.join('audio', 'sad.mp3'),
    'Surprise': os.path.join('audio', 'surprise.mp3')
}

while True:
    random_emotion = random.choice(emotions)
    print(random_emotion)
    
    audio_file = emotion_audio[random_emotion]
    playsound(audio_file)
    time.sleep(5)
