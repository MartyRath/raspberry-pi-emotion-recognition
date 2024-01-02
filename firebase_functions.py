# Uploads captured_images to firebase.
import firebase_admin
from firebase_admin import credentials, storage, db
import os
import datetime

# Function to initialise Firebase
def initialise_firebase():
    cred = credentials.Certificate('./serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'captured-emotion-images.appspot.com',
        'databaseURL': 'https://captured-emotion-images-default-rtdb.europe-west1.firebasedatabase.app/'
    })

    bucket = storage.bucket()
    img_ref = db.reference('/images')
    emotion_ref = db.reference('/emotions')
    
    return bucket, img_ref, emotion_ref

def upload_images_to_firebase(img_ref, bucket):
    # Lists filenames from captured_images directory
    image_filenames = os.listdir('captured_images')
    # Loop through image filenames
    for filename in image_filenames:
        # Check if the image has already been uploaded by comparing with Firebase storage
        blob = bucket.blob(filename)
        if not blob.exists():
            # Upload the image to Firebase Storage
            blob.upload_from_filename(os.path.join('captured_images', filename))
            print(f"Uploaded {filename} to Firebase Storage")

            current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            # Push file reference to image in Realtime DB
            img_ref.push({
                'image': filename,
                'timestamp': current_time
            })
    print ("Firebase images are up-to-date")


def upload_emotions_to_firebase(emotion_ref, emotion_label):
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    emotion_ref.push({
            'emotion': emotion_label,
            'timestamp': current_time
            })
    print("Emotion uploaded to firebase")