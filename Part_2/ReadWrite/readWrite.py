#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 23/07/19
# Purpose: To understand Read Write in Python and I guess a little bit
# more bash. 
#############################################################################

#############################################################################

import os

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################

#############################################################################
# Input: NULL
# This function returns CWD.
# Output: getcwd
#############################################################################

def createFile(name):
	cwd = os.getcwd()
	textfilePath = os.path.join(cwd, name+".txt")
	print(textfilePath)
	textFile = open(textfilePath,'a+')

	return textFile

name = 'bill'

file = createFile(name)
fileContent = file.read()
filelines = file.readlines() 
print(fileContent)
print(filelines)
file.close()
