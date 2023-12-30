# Emotion recognition with audio, capturing images when emotion changes, Blynk connectivity.

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

# Initialise pygame to play audio
pygame.init()

# Initialise Haar Cascade classifier for face detection
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Loads TFlite model into interpreter
emotion_interpreter = tf.lite.Interpreter(model_path="emotion_detection_model_100epochs.tflite")
# Allocates memory for the input and output tensors (multidimensional array structures) of the loaded model.
emotion_interpreter.allocate_tensors()

# Get input and output tensors (multidimensional array structures).
emotion_input_details = emotion_interpreter.get_input_details()
emotion_output_details = emotion_interpreter.get_output_details()

# Emotion labels to match what emotions TensorFlow Lite model was trained on.
class_labels=['Angry','Disgust', 'Fear', 'Happy','Neutral','Sad','Surprise']

# Captures video feed from the default webcam
video=cv2.VideoCapture(0)

# Initialise variable to store last detected emotion, and image number
last_emotion = None
image_count = 0

# Loops continuously to process video frames and predict emotions
while True:

    # .read() returns a boolean indicating if the frame was successfully read, and reads the current frame, 
    # e.g.(True, current_frame)
    ret,frame=video.read()
    
    # Converts frame to grayscale to improve face detection
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Uses Haar Cascade classifier to detect faces and outputs coordinates of detected face.
    # detectMultiScale allows detection at different scales, e.g. a face that is closer or further away
    faces=face_classifier.detectMultiScale(gray,1.3,5)

    # Iterates through detected face coordinates
    for (x,y,w,h) in faces:
        # print("Face detected!")
        # Extracts face (grayscale)
        face_gray=gray[y:y+h,x:x+w]
        # Resizes grayscale face to 48x48 as this is size tflite model was trained on. Interpolation maintains 
        # quality of image from resize
        face_gray=cv2.resize(face_gray,(48,48),interpolation=cv2.INTER_AREA)

        # Pre-processing detected face for tflite model prediction.
        face=face_gray.astype('float')/255.0  # Normalises data from [0, 255] to [0, 1]
        face=img_to_array(face) # Converts face to NumPy array
        # Expands the dimensions of array or tensor, i.e. face.
        # axis=0 adds a dimension to face, from a 2D frame of 48x48, to 3D 1x48x48.
        face=np.expand_dims(face,axis=0)
        
        # Sets the input tensor of the TensorFlow Lite interpreter with the processed face image.
        emotion_interpreter.set_tensor(emotion_input_details[0]['index'], face)
        # Invokes/runs the TensorFlow Lite interpreter to make emotion prediction.
        emotion_interpreter.invoke()
        # Retrieves the output tensor containing the predictions/results from the model inference.
        emotion_prediction = emotion_interpreter.get_tensor(emotion_output_details[0]['index'])

        # Assigns the highest value/most probable emotion from class_lables based on emotion_prediction
        emotion_label=class_labels[emotion_prediction.argmax()]

        # Prints the emotion only if it has changed from the last detection
        if emotion_label != last_emotion:
            print(emotion_label)
            last_emotion = emotion_label

            # Save image when emotion changes
            image_filename = f"captured_images/{emotion_label}_{image_count}.jpg"
            cv2.imwrite(image_filename, face_gray)
            print(f"Image saved as {image_filename}")
            image_count += 1

            # Connect to Blynk
            # As Blynk widget needs a number, dictionary to correspond emotion to number
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

            # Play emotion audio
            # Dictionary mapping emotions to audio files
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

            # Load the audio file
            audio = pygame.mixer.Sound(emotion_audio)
            # Play the audio file
            audio.play()

            # Checks if audio is still playing to allow it to play in full
            while pygame.mixer.get_busy():
                # Checks if audio still playing every 10 frames
                pygame.time.Clock().tick(10)
video.release()