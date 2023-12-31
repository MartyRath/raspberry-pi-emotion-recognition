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
from firebase_functions import initialise_firebase, upload_images_to_firebase, upload_emotions_to_firebase
from play_emotion_audio import play_emotion_audio
from emotion_to_blynk_number import emotion_to_number
import os

# Initialising Firebase and database directory references
bucket, img_ref, emotion_ref=initialise_firebase()

# Initialising Blynk
BLYNK_AUTH = 'Hm703ShkXO-pmualjhD1E6xaWBoDwjDH'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Emotion recognition
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
image_count = len(os.listdir('captured_images')) + 1

# Flag to control the emotion recognition loop
emotion_recognition_running = False

# Register handler for virtual pin V0 write event
@blynk.on("V0")
def write_handler(value):
    global emotion_recognition_running
    # Button controls if emotion recognition is on/off
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
            time.sleep(5)
            upload_images_to_firebase(img_ref, bucket)

# Main loop for emotion recognition
while True:
    if emotion_recognition_running:

        # .read() returns a boolean indicating if the frame was successfully read, and reads the current frame, 
        # e.g.(True, current_frame)
        ret, frame = video.read()

        # Converts frame to grayscale to improve face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Uses Haar Cascade classifier to detect faces and outputs coordinates of detected face.
        # detectMultiScale allows detection at different scales, e.g. a face that is closer or further away
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        # Iterates through detected face coordinates
        for (x, y, w, h) in faces:
            # Extracts just the face (grayscale) from image
            face_gray = gray[y:y+h, x:x+w]
            # Resizes grayscale face to 48x48 as this is size tflite model was trained on. Interpolation maintains 
            # quality of image from resize
            face_gray_resized = cv2.resize(face_gray, (48, 48), interpolation=cv2.INTER_AREA)

            # Pre-processing detected face for tflite model prediction.
            face = face_gray_resized.astype('float') / 255.0 # Normalises data from [0, 255] to [0, 1]
            face = img_to_array(face) # Converts face to NumPy array
            # Expands the dimensions of array or tensor, i.e. face.
            # axis=0 adds a dimension to face, from a 2D frame of 48x48, to 3D 1x48x48.
            face = np.expand_dims(face, axis=0)

            # Sets the input tensor of the TensorFlow Lite interpreter with the processed face image.
            emotion_interpreter.set_tensor(emotion_input_details[0]['index'], face)
            # Invokes/runs the TensorFlow Lite interpreter to make emotion prediction.
            emotion_interpreter.invoke()
            # Retrieves the output tensor containing the predictions/results from the model inference.
            emotion_prediction = emotion_interpreter.get_tensor(emotion_output_details[0]['index'])

            # Assigns the highest value/most probable emotion from class_lables based on emotion_prediction
            emotion_label = class_labels[emotion_prediction.argmax()]

            if emotion_label != last_emotion:
                print(emotion_label)
                last_emotion = emotion_label

                # Saves emotion label with timestamp to Firebase Realtime database
                upload_emotions_to_firebase(emotion_ref, emotion_label)

                # Saves processed image, face_gray, to captured_images
                image_filename = f"captured_images/{emotion_label}_{image_count}.jpg"
                cv2.imwrite(image_filename, face_gray_resized)
                print(f"Image saved as {image_filename}")
                image_count += 1

                # Converts emotion label to number for blynk image gallery
                emotion_number = emotion_to_number(emotion_label)
                blynk.run()
                blynk.virtual_write(1, emotion_number)

                play_emotion_audio(emotion_label)


    # Run Blynk
    blynk.run()
    time.sleep(0.5)

# Release resources
video.release()
cv2.destroyAllWindows()
