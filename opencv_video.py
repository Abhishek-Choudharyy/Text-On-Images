import numpy as np  
import cv2  
import dlib  
import openface
import time

import face_recognition.api as face_recognition
from image_embedding import image_similarity

video_capture = cv2.VideoCapture('test2.mp4')

cascade_path = "Face-Detection-OpenCV/data/haarcascade_frontalface_alt.xml"  
predictor_path= "shape_predictor_68_face_landmarks.dat"  
defaultModel = "openface/models/openface/nn4.v1.t7"
net = openface.TorchNeuralNet(model = defaultModel, imgDim =96)
   
# Create the haar cascade  
faceCascade = cv2.CascadeClassifier(cascade_path)  
   
# create the landmark predictor  
predictor = dlib.shape_predictor(predictor_path)  
face_aligner = openface.AlignDlib(predictor_path)

i = 0
start = time.time()
while True:
    i = i + 1
    # Grab a single frame of video
    ret, frame = video_capture.read()
    print(ret)
    if (not ret):
        break
# Resize frame of video to 1/4 size for faster face recognition processing
    image = cv2.resize(frame, (0, 0), fx=0.35, fy=0.35)
    
    # convert the image to grayscale  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
       
    # Detect faces in the image  
    faces = faceCascade.detectMultiScale(  
       gray,  
       scaleFactor=1.05,  
       minNeighbors=5,  
       minSize=(100, 100),  
       flags=cv2.CASCADE_SCALE_IMAGE  
    ) 
    
    encodings = face_recognition.face_encodings(image)
    print("Found {0} faces!".format(len(faces)))  
    # Region of interest only one face at a time and recognizeing that face
    # ALigned Face for recognization par
    # Draw a rectangle around the faces  
    for (x, y, w, h) in faces:  
       cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)    
       roi = image[y:y+h, x:x+w]
       alignedFace = face_aligner.align(534, roi, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
       result = image_similarity(image)
       font = cv2.FONT_HERSHEY_SIMPLEX
       for k,v in result.items():
           print(k,v)
           text = str(k) + "(" + str(v) +")"
           cv2.putText(image, text , (x,y+h), font, 0.5, (255,255,0), 2, cv2.LINE_AA)

    
 # copying the image so we can see side-by-side  
    image_copy = image.copy()  
    


    # Display the resulting image
    cv2.imshow('Video', image_copy)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

   



