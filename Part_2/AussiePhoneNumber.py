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

#0412 235 235

def isAussieNumber(phoneNumber):
	RemovedphoneNumber = phoneNumber.replace(' ', '')
	if len(RemovedphoneNumber) != 10:
		print("Length needs to be 12.")
		return False
	for i in range(0,4):
		# print(phoneNumber[i]) #DEBUG
		if RemovedphoneNumber[i].isalpha():
			print("Phonenumber contains letters. ")
			return False
	for i in range(5,7):
		if RemovedphoneNumber[i].isalpha():
			print("Phone number contains letters. ")
			return False
	for i in range(7,10):
		if RemovedphoneNumber[i].isalpha():
			print("Phone number contains letters. ")
			return False
	return True


#############################################################################
# 								Main Code. 
#############################################################################

print("The number should follow the following format: 04xx xxx xxx")

phoneNumber = input("Please input a Australian Phone Number: ")

while phoneNumber != "":
	if isAussieNumber(phoneNumber):
		print(phoneNumber, "is valid.")
	phoneNumber = input("Please input a Australian Phone Number: ")
