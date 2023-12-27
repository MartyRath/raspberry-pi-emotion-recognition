import random
import time
import pygame
import os

# Initialise pygame
pygame.init()

emotion_text = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Dictionary mapping emotions to audio files
emotion_text_to_audio = {
    'Angry': os.path.join('audio', 'angry.mp3'),
    'Disgust': os.path.join('audio', 'disgust.mp3'),
    'Fear': os.path.join('audio', 'fear.mp3'),
    'Happy': os.path.join('audio', 'happy.mp3'),
    'Neutral': os.path.join('audio', 'sad.mp3'),
    'Sad': os.path.join('audio', 'sad.mp3'),
    'Surprise': os.path.join('audio', 'surprise.mp3')
}

while True:
    random_emotion = random.choice(emotion_text)
    print(random_emotion)
    emotion_audio = emotion_text_to_audio[random_emotion]

    # Load the audio file
    audio = pygame.mixer.Sound(emotion_audio)
    
    # Play the audio file
    audio.play()

    # Checks if audio is still playing to allow it to play in full
    while pygame.mixer.get_busy():
        # Checks if audio still playing every 10 frames
        pygame.time.Clock().tick(10)

    time.sleep(5)