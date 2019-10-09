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
import pickle
import time
#############################################################################
# Input: input
# This function DOES
# Output: input
#############################################################################

def SVMRegression(X, y, output):

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=109)
	#print(X_train)
	#print(y_train)
	start_time = time.time()
	svclassifier = svm.SVC(kernel='rbf', degree=4, gamma='auto_deprecated', max_iter = 10, tol=0.001)

	print("Fitting the data.")
	print("##################################################")
	svclassifier.fit(X_train, y_train) 
	print("--- %s seconds to complete ---" % (time.time() - start_time))
	print("Fitment Complete. Moving onto the Prediciton.")
	print("##################################################")

	y_pred = svclassifier.predict(X_test)
	start_time = time.time()
	print("--- %s seconds to complete ---" % (time.time() - start_time))
	#y_pred.to_csv(y_pred,"Prediction" sep=',', low_memory=False)

	file = open(output+"_score.txt", 'w')

	print("##################################################")
	print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
	print("Precision:",metrics.precision_score(y_test, y_pred))
	print("Recall:",metrics.recall_score(y_test, y_pred))
	print("F Score:",metrics.f1_score(y_test, y_pred))

	file.write("##################################################")
	file.write("\nAccuracy:" + str(metrics.accuracy_score(y_test, y_pred)))
	file.write("\nPrecision:" + str(metrics.precision_score(y_test, y_pred)))
	file.write("\nRecall:" + str(metrics.recall_score(y_test, y_pred)))
	file.write("\nF Score:" + str(metrics.f1_score(y_test, y_pred)))

	file.close()

	dmp = pickle.dump(svclassifier, open(output + '.sav','wb'))
	np.savetxt(output + ".csv", y_pred, delimiter=",")

def pandasLoad(filename):
	data = pd.read_csv("Inputs/"+ filename + '.csv', sep=',', low_memory=False)
	X = data.drop(["QuoteConversion_Flag", "Original_Quote_Date"],axis=1)
	y = data['QuoteConversion_Flag']
	return X, y

#############################################################################
# 								Main Code. 
#############################################################################

filename = "SMOTEdProcessed"

X, y = pandasLoad(filename)

SVMRegression(X, y, "Outputs/rbfPrediction")