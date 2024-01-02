# Provides dictionary to convert emotion label to number for Blynk image gallery to 
# show appropriate emoticon image

def emotion_to_number(emotion_label):
    emotion_to_number = {
                    'Angry': 0,
                    'Disgust': 1,
                    'Fear': 2,
                    'Happy': 3,
                    'Neutral': 4,
                    'Sad': 5,
                    'Surprise': 6
                }
    emotion_number = emotion_to_number[emotion_label]
    return emotion_number