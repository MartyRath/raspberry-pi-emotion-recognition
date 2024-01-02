# Plays appropriate audio file based on emotion_label
import os
import subprocess

def play_emotion_audio(emotion_label):
    emotion_text_to_audio = {
        'Angry': os.path.join('audio', 'angry.mp3'),
        'Disgust': os.path.join('audio', 'disgust.mp3'),
        'Fear': os.path.join('audio', 'fear.mp3'),
        'Happy': os.path.join('audio', 'happy.mp3'),
        'Neutral': os.path.join('audio', 'neutral.mp3'),
        'Sad': os.path.join('audio', 'sad.mp3'),
        'Surprise': os.path.join('audio', 'surprise.mp3')
    }

    emotion_audio = emotion_text_to_audio[emotion_label]
    print(f"Playing audio file: {emotion_audio}")
    subprocess.run(['paplay', emotion_audio])