#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 12/07/19
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

def myFileStructure():
	CWD = "/mnt/c/Coding/Github/ReLearningPython/Part_2/ReadWrite"
	getcwd = os.getcwd()
	print("The Path is " + CWD+"\n"+ "The CWD is " + getcwd)
	print(os.listdir(getcwd))
	print(os.path.getsize(getcwd))
	

	
	return getcwd

	

#############################################################################
# 								Main Code. 
#############################################################################

CWD = myFileStructure()
print(CWD)