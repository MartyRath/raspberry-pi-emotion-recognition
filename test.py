"""
Live prediction of emotion using pre-trained models. 
Uses haar Cascades classifier to detect face..
then, uses pre-trained models for emotion to predict them from 
live video feed. 

Prediction is done using tflite models. 
Note that tflite with optimization takes too long on Windows, so not even try.
Try it on edge devices, including RPi. 

"""

from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import tensorflow as tf

face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#### PREDICT USING tflite ###

# Load the TFLite model and allocate tensors.
emotion_interpreter = tf.lite.Interpreter(model_path="emotion_detection_model_100epochs.tflite")
emotion_interpreter.allocate_tensors()

# Get input and output tensors.
emotion_input_details = emotion_interpreter.get_input_details()
emotion_output_details = emotion_interpreter.get_output_details()

# Test the model on input data.
emotion_input_shape = emotion_input_details[0]['shape']

#frame = cv2.imread('obamas.jpg')
###########################

class_labels=['Angry','Disgust', 'Fear', 'Happy','Neutral','Sad','Surprise']

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    labels=[]
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

        #Get image ready for prediction
        roi=roi_gray.astype('float')/255.0  #Scale
        roi=img_to_array(roi)
        roi=np.expand_dims(roi,axis=0)  #Expand dims to get it ready for prediction (1, 48, 48, 1)
        
        emotion_interpreter.set_tensor(emotion_input_details[0]['index'], roi)
        emotion_interpreter.invoke()
        emotion_preds = emotion_interpreter.get_tensor(emotion_output_details[0]['index'])

        #preds=emotion_model.predict(roi)[0]  #Yields one hot encoded result for 7 classes
        emotion_label=class_labels[emotion_preds.argmax()]  #Find the label
        emotion_label_position=(x,y)
        cv2.putText(frame,emotion_label,emotion_label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        print(emotion_label)    
    
    cv2.imshow('Emotion Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #Press q to exit
        break
cap.release()
cv2.destroyAllWindows()


##############################
