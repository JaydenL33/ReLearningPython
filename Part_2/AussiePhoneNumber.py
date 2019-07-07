#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 7/07/19
# Purpose: To find whether a phone number is an Australian PhoneNumber
#############################################################################

#############################################################################
# 							Function Defining.
#############################################################################

#############################################################################
# Input: input
# This function DOES
# Output: input
#############################################################################



def isAussieNumber(phoneNumber):
	for i in range(0,5):
		print(phoneNumber[i])
		if phoneNumber[i].isalpha():
			return False
	for i in range(6,10):
		if phoneNumber[i].isalpha():
			return False
	for i in range(9,12):
		if phoneNumber[i].isalpha():
			return False
	return True


#############################################################################
# 								Main Code. 
#############################################################################

print("The number should follow the following format: 04xx xxx xxx")

phoneNumber = input("Please input a Australian Phone Number!.")

while phoneNumber not "\n":
	if isAussieNumber(phoneNumber):
		print(phoneNumber, "is valid.")
	phoneNumber = input("Please input a Australian Phone Number!.")