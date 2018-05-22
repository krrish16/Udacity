#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC( C = 10000.0 ,kernel = "rbf")   #linear kernel gives more accuracy
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t0 = time()
pred = clf.predict(features_test)
print "Prediction time:", round(time()-t0, 3), "s"
print pred[10],pred[26],pred[50]
c = 0
for x in range(len(pred)):
    if pred[x] == 1:
	    c = c+1
print c
print "Predictiob time:", round(time()-t0, 3), "s"
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc
#########################################################


