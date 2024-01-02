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
