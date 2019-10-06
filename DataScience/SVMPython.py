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

#############################################################################
# Input: input
# This function DOES
# Output: input
#############################################################################

def SVRegression(data):
	X = data[:,1:]
	y = data[:,0]
	clf = svm.SVR()
	clf.fit(X, y) 
	SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1,
	    gamma='auto_deprecated', kernel='rbf', max_iter=-1, shrinking=True,
	    tol=0.001, verbose=False)
	clf.predict([[1, 1]])
	array([1.5])

def pandasLoad(filename):
	data = pd.read_csv(filename + '.csv', sep=',',header=None)
	return data

#############################################################################
# 								Main Code. 
#############################################################################

filename = "LearningSetSVM"

data = pandasLoad(filename)

print(data)

SVRegression(data)