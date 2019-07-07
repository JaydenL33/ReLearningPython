#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 7/07/19
# Purpose: This is a code lock checker. It checks to see if the code lock is
# right one. 
#############################################################################

#############################################################################
# Function Defining
#############################################################################

#############################################################################
# Input: CODE
# This function checks if the code lock is correct. 
#############################################################################

def CodeCheck(CODE):
	if CODE == 2153:
		print("You got the Code!")
		return 1
	else:
		print("You got the code wrong!")
		return 0


#############################################################################
# Main Code. 
#############################################################################
userCode = ""
finalCode = 0 

while CodeCheck(finalCode) == 0: 
	while len(userCode) != 4:
		print(str(len(userCode))) # Debug
		digit = input("Enter one Digit: ")
# Conditions!
		if len(digit) > 1:
			print("Only one Digit.")
		if digit.isalpha():
			print("Only numbers.")
		else:
			userCode = userCode + digit
			print("Reached %s.", userCode) # Debug
	finalCode = int(userCode)
	userCode = ""





