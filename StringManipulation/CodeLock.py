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
		return True
	else:
		print("You got the code wrong!")
		return False


#############################################################################
# Main Code. 
#############################################################################
userCode = ""
finalCode = 0 

print("The Code will loop if you got the code wrong.")
while CodeCheck(finalCode) == False: 

	while len(userCode) != 4:
		print(str(len(userCode)))
		digit = input("Enter one Digit: ")
# Conditions!
		if len(digit) > 1:
			print("Only one Digit.")
		if digit.isalpha():
			print("Only numbers.")
		else:
			print("Reached %s.", userCode)
			userCode = userCode + digit
			

	finalCode = int(userCode)





