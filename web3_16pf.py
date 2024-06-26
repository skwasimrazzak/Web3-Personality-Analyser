# -*- coding: utf-8 -*-
"""Web3_16pf.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VRxKr4gYwRINX1xPBO9j3cYNuQ4_LBcs
"""

#REQUIRED LIBRARIES IMPORTED
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("FinalDataset.csv").drop("Analysis", axis=1) #reads the dataset without the 1st column

df.head() #displays the dataset

df.columns #displays the column heading with no. of columns and datatypes

TARGETS = ['Anxiety', 'Independence', 'Extroversion', 'Tough_Mindness', 'Self_Control'] #list storing the target variables

X = df.drop(TARGETS, axis=1) #list for storing the input features
y = df[TARGETS] #list for storing the target/output variables

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100) #splits dataset for training and testing

#SCALING OF DATASET (PRE-PROCESSING)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#IMPORTING LIBRARIES OF MODELS
from sklearn.metrics import accuracy_score
from sklearn.multioutput import MultiOutputClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

models = [DecisionTreeClassifier(), RandomForestClassifier(), SVC()] #list storing ML models to be used

#DISPLAYING ACCURACY OF DIFFERENT MODELS FOR OUR DATASET
for model in models:
    multi_model = MultiOutputClassifier(model)
    multi_model.fit(X_train, y_train)
    acc = multi_model.score(X_test, y_test)
    print(f"Model: {model} \t Accuracy: {acc}")

#FITTING THE BEST MODEL FOR OUR DATASET
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

predicted = rf.predict(X_test) #predicting from test data after separately fitting in model

for i in predicted:#display predictions
  print(i)

#Make new data for finding output
import random
outerArr = []
for j in range(5):
  innerArr = []
  for i in range(110):
    randomElement = random.randrange(0,20)
    innerArr.append(randomElement)
  outerArr.append(innerArr)

print(outerArr)
for i in outerArr:
  print(i)

#predicting
Arr = []
for i in range(5):
  # Arr = df.drop(outerArr[i], axis=1)
  # Arr = outerArr[i]
  scaler = StandardScaler()
  Arr = scaler.fit_transform(outerArr)

predicted2 = rf.predict(Arr)
for i in predicted2:
  print(i)

import joblib

model_path = 'random_forest_model.pkl'  # Change the path and filename
joblib.dump(rf, model_path)