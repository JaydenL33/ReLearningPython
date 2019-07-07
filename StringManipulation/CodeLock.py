#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 7/07/19
# Purpose: This is a code lock checker. It checks to see if the code lock is
# right one. 
#############################################################################

#############################################################################
# 							Function Defining
#############################################################################

#############################################################################
# Input: CODE
# This function checks if the code lock is correct. 
#############################################################################

def CodeCheck(CODE, FIRSTRUN):
	if CODE == 2153 and FIRSTRUN == False:
		print("You got the Code!")
		return True
	elif FIRSTRUN == True:
		return False
	else:
		print("You got the code wrong!")
		return False


#############################################################################
# 								Main Code. 
#############################################################################
userCode = ""
finalCode = 0
check = True

while CodeCheck(finalCode, check) == False:
	check = False
	while len(userCode) != 4:
		
		digit = input("Enter one Digit: ")
# Conditions!
		if len(digit) > 1:
			print("Only one Digit.")
		if digit.isalpha():
			print("Only numbers.")
		else:
			userCode = userCode + digit
			

	finalCode = int(userCode)
	userCode = ""





