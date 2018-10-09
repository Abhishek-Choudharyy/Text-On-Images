#Download image from google images according to Name
import time

from bs4 import BeautifulSoup

##pip3 install face_recognition
import face_recognition
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

import urllib
from urllib.request import urlopen


#To open Headless Browser
df = pd.DataFrame()
i = 0
name = input("Enter Name: ")    # Name input eg: Ross Geller

driver = webdriver.Firefox()
driver.implicitly_wait(30)

file_name = name.replace(" ","_")
base_url = "https://www.google.co.in/search?tbm=isch&q=" + str(urllib.parse.quote(name))
driver.get(base_url)
time.sleep(2)
html_source = driver.page_source
soup = BeautifulSoup(html_source,"lxml")
for abc in soup.find_all("div",attrs={"jscontroller":"Q7Rsec"}):
    print(i)
    try:
        url = abc.find("img", attrs={"class":"rg_ic rg_i"})["data-src"]
        # Using solo images only by counting number of faces in image
        if(len(face_recognition.face_encodings(face_recognition.load_image_file(urlopen(url)))) == 1):
            print(i,len(face_recognition.face_encodings(face_recognition.load_image_file(urlopen(url)))))
            df.loc[i,'url'] = url
            filename = "image_data/" + str(file_name) + "/" + str(file_name) +"_" +str(i) + ".jpg"
            urllib.request.urlretrieve(url, filename)
            i = i + 1
            # Using first 200 images
            if(i > 200):
                break
    except:
        pass
##Please check once manually all images
df.to_csv("image_data/" + str(file_name) + "/" + str(file_name) + ".csv")
driver.close()




