#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 6/10/19
# Purpose: To use a SVM for our regression problem. 
# Source: 
# In Source Documentation
#############################################################################

#############################################################################

from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics

#############################################################################
# Input: input
# This function DOES
# Output: input
#############################################################################

def SVMRegression(X, y):

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=109)

	#print(y)
	clf = svm.SVC(kernel='linear')
	print("Fitting Data")
	clf.fit(X_train, y_train) 
	print("Fitment Complete, Moving onto the Prediciton.")
	y_pred = clf.predict(X_Test)
	print(y_pred)
	print("##################################################")
	print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
	print("Precision:",metrics.precision_score(y_test, y_pred))
	print("Recall:",metrics.recall_score(y_test, y_pred))


def pandasLoad(filename):
	data = pd.read_csv(filename + '.csv', sep=',', low_memory=False)
	X = data.drop(["QuoteConversion_Flag"],axis=1)
	X = data.drop(["Quote_ID"],axis=1)
	X = data.drop(["Original_Quote_Date"],axis=1)
	y = data['QuoteConversion_Flag']
	return X, y

#############################################################################
# 								Main Code. 
#############################################################################

filename = "LearningSetSVM"

X, y = pandasLoad(filename)

SVMRegression(X, y)