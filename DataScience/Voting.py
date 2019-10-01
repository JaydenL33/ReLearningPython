#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 1/10/2019
# Purpose: In order to vote on the predicited values, I've used a vote. 
# Meaning that if the the values occur more then 3 times, then it will be the
# final voted value.
#############################################################################

#############################################################################

import csv

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################
class otherClass:
    def __init__(self):
    	self.x = 10
    	self.str = "HELLO!"

    def getData(self):
        print("{0}+{1}j".format(self.x,self.x))


#############################################################################
# Input: Tables(The List of Tables), 
# n (Being the of tables gone through already)
# This function DOES
# Output: input
#############################################################################

def CSVLoad(tables, n):
	with open(name + ".csv", 'r') as Voting:
		read_data = csv.reader(Voting)

	for i in range(read_data):
		tables[i[n]] = int(read_data[i+1[2]])
	return tables

#############################################################################
# Input: input
# This function DOES
# Output: input
#############################################################################

def Voting(tables, finalTable):

	for i in range(tables):
		for l in range(tables[i]):
			entrySum += tables[i[l]]
		if entrySum >= 3:
			finalTable[i] = 1
	return finalTable




#############################################################################
# 								Main Code. 
#############################################################################

finalTable = []
tables = []