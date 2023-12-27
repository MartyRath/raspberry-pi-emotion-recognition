import random
import time
import playsound
import os

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

while True:
    random_emotion = random.choice(emotions)
    print(random_emotion)
    time.sleep(5)  # Wait for 5 seconds before generating the next emotion

# Dictionary mapping emotions to audio file names or paths
emotion_audio = {
    'Angry': os.path.join('audio', 'angry.m4a'),
    'Disgust': os.path.join('audio', 'disgust.m4a'),
    'Fear': os.path.join('audio', 'fear.m4a'),
    'Happy': os.path.join('audio', 'happy.m4a'),
    'Neutral': os.path.join('audio', 'sad.m4a'),
    'Sad': os.path.join('audio', 'sad.m4a'),
    'Surprise': os.path.join('audio', 'surprise.m4a')
}

audio_file = emotion_audio[random_emotion]
playsound(audio_file)