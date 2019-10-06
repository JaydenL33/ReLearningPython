#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 6/10/19
# Purpose: To use a SVM for our regression problem. 
# Source: 
# https://www.datacamp.com/community/tutorials/svm-classification-scikit-learn-python
# https://www.youtube.com/watch?v=1NxnPkZM9bc
# https://scikit-learn.org/stable/modules/svm.html
# https://stackoverflow.com/questions/11023411/how-to-import-csv-data-file-into-scikit-learn
#############################################################################

#############################################################################

from sklearn import svm
import numpy as np


#############################################################################
# Input: input
# This function DOES
# Output: input
#############################################################################

def SVRegression():
	X = [[0, 0], [2, 2]]
	y = [0.5, 2.5]
	clf = svm.SVR()
	clf.fit(X, y) 
	SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1,
	    gamma='auto_deprecated', kernel='rbf', max_iter=-1, shrinking=True,
	    tol=0.001, verbose=False)
	clf.predict([[1, 1]])
	array([1.5])

def npLoad():
	f = open("filename.txt")
	f.readline()  # skip the header
	data = np.loadtxt(f)
	return data

#############################################################################
# 								Main Code. 
#############################################################################

