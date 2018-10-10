## Text-On-Images
Python Imaging Library (PIL)


**pip install pillow**
-  For creating ImageFont objects we also need font(ttf, otf) files (font can be downloaded from GitHub repo: https://github.com/google/fonts/tree/master/apache/roboto )
- Computer graphics have an inverted coordinate system, the origin(0, 0) that lies at the top-left corner of the image. x here represents the distance of the text box from the left (x=0) and y represents the distance from the top (y=0)
- While you save the image, you can pass optional parameters like optimize and quality to control the size of the output image.

Source : https://haptik.ai/tech/putting-text-on-image-using-python/


## Downloading Images from google Images according to user input
file: google_images.py

**pip install face_recognition** (https://github.com/ageitgey/face_recognition) 
Using Selenium, Bs4 and face-recognition API 
Input : Name
Output : Solo Images of the input from google images

We are also saving all the downloaded image URLs

## Find Face Embedding from URL

Source : https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
file : image_to_embedding.py

Input : Image URL
Output : Face Embedding for only solo images


## Compare Similarity in Faces

file : image_embedding.py

Using KNN to find similar class for given image according to embeddings (https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/)

## Run Face Recognition on Videos
file: opencv_video.py

Output : result.mp4





