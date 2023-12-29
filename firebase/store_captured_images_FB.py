# Uploads captured_images to firebase.
import firebase_admin
from firebase_admin import credentials, storage
import os

cred=credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'captured-emotion-images.appspot.com',
    'databaseURL': 'https://captured-emotion-images-default-rtdb.europe-west1.firebasedatabase.app/'
})

bucket = storage.bucket()

captured_images_path = '../captured_images'

# Returns list of current image filenames 
image_filenames = os.listdir(captured_images_path)

# Loop through image filenames
for filename in image_filenames:
    # Check if the image has already been uploaded by comparing with Firebase storage
    blob = bucket.blob(filename)
    if not blob.exists():
        # Upload the image to Firebase Storage
        blob.upload_from_filename(os.path.join(captured_images_path, filename))
        print(f"Uploaded {filename} to Firebase Storage")

print ("Firebase up-to-date")
