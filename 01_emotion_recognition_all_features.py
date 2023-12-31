"""
Realtime prediction of emotion using pre-trained models via webcam feed.
Models:
Haar Cascade Classifier from OpenCV to detect faces.
TensorFlow Lite model trained from Kaggle images to predict emotions.
"""

import tensorflow as tf
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import BlynkLib

import time
import pygame
import os

BLYNK_AUTH = 'Hm703ShkXO-pmualjhD1E6xaWBoDwjDH'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Workaround to get pygame to work headless
os.putenv('SDL_VIDEODRIVER', 'fbcon')
# Initialise pygame to play audio
pygame.init()

# Initialise Haar Cascade classifier for face detection
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Loads TFlite model into interpreter
emotion_interpreter = tf.lite.Interpreter(model_path="emotion_detection_model_100epochs.tflite")
# Allocates memory for the input and output tensors (multidimensional array structures) of the loaded model.
emotion_interpreter.allocate_tensors()

# Get input and output tensors (multidimensional array structures).
emotion_input_details = emotion_interpreter.get_input_details()
emotion_output_details = emotion_interpreter.get_output_details()

# Emotion labels to match what emotions TensorFlow Lite model was trained on.
class_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Captures video feed from the default webcam
video = cv2.VideoCapture(0)

# Initialise variable to store last detected emotion, and image number
last_emotion = None
image_count = 0

# Flag to control the emotion recognition loop
emotion_recognition_running = True

# register handler for virtual pin V0 write event
@blynk.on("V0")
def write_handler(value):
    global emotion_recognition_running
    buttonValue = value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue == "1":
        if not emotion_recognition_running:
            print("Starting emotion recognition")
            emotion_recognition_running = True
        else:
            print("Emotion recognition already running.")

    else:
        if emotion_recognition_running:
            print("Stopping emotion recognition...")
            emotion_recognition_running = False

# Main loop for emotion recognition
while True:
    if emotion_recognition_running:
        ret, frame = video.read()

        # Converts frame to grayscale to improve face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Uses Haar Cascade classifier to detect faces and outputs coordinates of detected face.
        # detectMultiScale allows detection at different scales, e.g. a face that is closer or further away
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_gray = gray[y:y+h, x:x+w]
            face_gray_resized = cv2.resize(face_gray, (48, 48), interpolation=cv2.INTER_AREA)

            face = face_gray_resized.astype('float') / 255.0
            face = img_to_array(face)
            face = np.expand_dims(face, axis=0)

            emotion_interpreter.set_tensor(emotion_input_details[0]['index'], face)
            emotion_interpreter.invoke()
            emotion_prediction = emotion_interpreter.get_tensor(emotion_output_details[0]['index'])

            emotion_label = class_labels[emotion_prediction.argmax()]

            if emotion_label != last_emotion:
                print(emotion_label)
                last_emotion = emotion_label

                image_filename = f"captured_images/{emotion_label}_{image_count}.jpg"
                cv2.imwrite(image_filename, face_gray)
                print(f"Image saved as {image_filename}")
                image_count += 1

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
                blynk.run()
                blynk.virtual_write(1, emotion_number)

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

                audio = pygame.mixer.Sound(emotion_audio)
                audio.play()

                while pygame.mixer.get_busy():
                    pygame.time.Clock().tick(10)

    # Run Blynk
    blynk.run()
    time.sleep(0.5)

# Release resources
video.release()
pygame.mixer.stop()
cv2.destroyAllWindows()
