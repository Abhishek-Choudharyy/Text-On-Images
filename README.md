## Text-On-Images
Python Imaging Library (PIL)


- **pip install pillow**
-  For creating ImageFont objects we also need font(ttf, otf) files (font can be downloaded from GitHub repo: https://github.com/google/fonts/tree/master/apache/roboto )
- Computer graphics have an inverted coordinate system, the origin(0, 0) that lies at the top-left corner of the image. x here represents the distance of the text box from the left (x=0) and y represents the distance from the top (y=0)
- While you save the image, you can pass optional parameters like optimize and quality to control the size of the output image.

Source : https://haptik.ai/tech/putting-text-on-image-using-python/


## Downloading Images from google Images according to user input
Using Selenium, Bs4 and face-recognition API (https://github.com/ageitgey/face_recognition) (google_images.py)
Input : Name
Output: Solo Images of the input from google images
