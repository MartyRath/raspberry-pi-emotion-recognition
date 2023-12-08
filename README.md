# raspberry-pi-emotion-recognition
Project Name: The "How's it going?" Hat - Using a Raspberry Pi with camera for emotion recognition

Introduction

My partner is autistic and often has trouble interpreting emotion.
The purpose of this project is to develop a device that can
interpret emotion in real-time via a camera and communicate those 
emotions with the user. The device is aimed at users who have 
trouble recognising facial expressions. 
Baseline:
- The device recognises two emotions, e.g., happy/sad, with a delay.
- Sends the emotion as text to the user via a web app.
Depending on time constraints:
- Communicate emotions to user via Bluetooth earphones.
- Be "discreetly" mounted in a hat.
- Recognise multiple emotions in real-time.
- Web app will show the emotion as an emoticon and in text.
- Use IoT platform such as ThingSpeak

Tools, Technologies, and Equipment
Hardware
- Processing: Raspberry Pi 4 Model B
- Sensor: Raspberry Pi v2.1 Camera
Programming
- Device: Windows 10 computer
- IDE: Visual Studio Code to remotely access Pi via SSH
- Language: Python
Emotion Recognition
- Face detection: OpenCV
- Emotion recognition: TensorFlow Lite
Communication from Pi to Web-App
- MQTT
- IoT Platform such as ThingSpeak
