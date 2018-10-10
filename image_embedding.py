#To make a face recognition model to detect similairty between image and friends character
#code : {0: Chandler Bing: 1: Joey Tribbiani; 2:Monica Geller; 3:Phoebe Buffay; 4:Rachel Green; 5:Ross Geller}
import pandas as pd
import numpy as np
import face_recognition
from urllib.request import urlopen

##Sklearn for algo and split in data
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn import metrics
import cv2

def image_similarity(image):
# =============================================================================
#     df = pd.read_csv("image_url.csv")
# =============================================================================
    
    known_face_names = [
        "Chandler Bing",
        "Joey Tribbiani",
        "Monica Geller",
        "Phoebe Buffay",
        "Rachel Green",
        "Ross Geller",
    ]
    
# =============================================================================
#     train_Y= pd.DataFrame()
#     train_Y["output"]= df["code"]
#     train_Y["url"] = df["url"]
# =============================================================================
    
    column_new = list()
    for k in range(128):
        column_new.append("column_"+str(k))
        
    train_X = pd.DataFrame(columns=column_new)

    
    data = pd.read_csv("train_X.csv")
    train_y = pd.read_csv("train_Y.csv")
    
    data = data.drop(columns=['url','Unnamed: 0'])
    
    X_train, X_test, y_train, y_test = train_test_split(data, train_y["output"], test_size=0.33, random_state=42)
    
    
    #Create KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=7)
    
    #Train the model using the training sets
    knn.fit(X_train, y_train)
    


    test = list()
    try:
        test = face_recognition.face_encodings(image)

    except:
        pass
    result = dict()
    for i in range(len(test)):
        check = pd.DataFrame(test[i].reshape(-1, len(test[i])), columns=column_new)
        train_X.loc[0] = check.loc[0]
        result[known_face_names[int(knn.predict(train_X))]] = round((1.00 - np.average(knn.kneighbors(train_X)[0]))*100, 2)

    return(result)





