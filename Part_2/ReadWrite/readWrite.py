#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 23/07/19
# Purpose: Creating and reading files.
#############################################################################

#############################################################################

import os

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################

#############################################################################
# Input: 'name of the file.'
# This creates a file with any specified name. 
# Output: the opened file 'textFile'
#############################################################################


def updateAndRead(toCheck, name, toUpdate):
	toCheck.read()
	# Write Data to it here #
	toCheck.write("\n"+toUpdate)
	toCheck.close()
	toCheck = createFile(name, 0)
	checking = toCheck.read()
	print(checking)
	toCheck.close()



def createFile(name, toggle):
	cwd = os.getcwd()
	textfilePath = os.path.join(cwd, name+".txt")
	# print(textfilePath)
	# Therefore can be local path and doesn't require import os. 
	localPath = name+".txt"
	if toggle == 0:
		textFile = open(localPath,'r+')
	if toggle == 1: 
		textFile = open(localPath,'a')

	return textFile



name = 'bill'

file = createFile(name, 0)
toUpdate = input("Please input Data for the file: ")
updateAndRead(file, name, toUpdate)


