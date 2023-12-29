# Uploads captured_images to firebase.
import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import os

cred=credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'captured-emotion-images.appspot.com',
    'databaseURL': 'https://captured-emotion-images-default-rtdb.europe-west1.firebasedatabase.app/'
})

bucket = storage.bucket()

captured_images = '../captured_images'

# Function returns list of current image filenames 
def get_image_filenames(captured_images):
    image_filenames = []
    for filename in os.listdir(captured_images):
        image_filenames.append(filename)
        print(image_filenames)
    return image_filenames

get_image_filenames(captured_images)