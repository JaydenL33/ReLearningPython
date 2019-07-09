#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 7/07/19
# Purpose: To find whether a phone number is an Australian Phone-Number
#############################################################################

#############################################################################
# 							Function Defining.
#############################################################################

#############################################################################
# Input: phoneNumber String
# This function checks if the phoneNumber is an Australian Phone Number
# Output: True or False
#############################################################################


def isAussieNumber(phoneNumber):
	RemovedphoneNumber = phoneNumber.replace(' ', '')
	if len(RemovedphoneNumber) != 10:
		#print("Length needs to be 12.")
		return False
	for i in range(0,4):
		# print(phoneNumber[i]) #DEBUG
		if RemovedphoneNumber[i].isalpha():
			#print("Phonenumber contains letters. ")
			return False
	for i in range(5,7):
		if RemovedphoneNumber[i].isalpha():
			#print("Phone number contains letters. ")
			return False
	for i in range(7,10):
		if RemovedphoneNumber[i].isalpha():
			#print("Phone number contains letters. ")
			return False
	return True

def insideMessage(text):
	for i in range(len(text)):
		chunk = text[i:i+12]
		if isAussieNumber(chunk) == True:
			print(chunk, "is an Australian Phone Number.")

#############################################################################
# 								Main Code. 
#############################################################################
"""
print("The number should follow the following format: 04xx xxx xxx")

phoneNumber = input("Please input a Australian Phone Number: ")

while phoneNumber != "":
	if isAussieNumber(phoneNumber):
		print(phoneNumber, "is valid.")
	phoneNumber = input("Please input a Australian Phone Number: ")
"""

message = """0458 770 196 is my phone number. Call me. or don't. 
awdojawijdjiawdjiawdjiaw awopd jawipdj waipdjwaip djwpdijw ijdw j
dhawdwadhawdoiahdoawhd 8wadh awodh awoudh waoudh waoudh 
awdhawd98hawd8 hawd8 ahwd8awh d8wad
02309 39492384892 39324 0412 234 232 2039239819382389231
bad number man.""" # DOESNT WORK


message = """1 Hour @ Lighthouse $50 | Helping Patrick Setup new Machine and migration of old data. Kerio Setup

2 Hours @ Lighthouse $100 | Taking the old machine, setup of the new Lenovo All in One

2 Hour @ Lighthouse $100 | Data Recovery and Backup for the Old Machine

1.5 Hours (Only change one hour because of miscommunication) @ totemo $50 | Consultation with Martin about the NAS, and the external drives bought. Fixed and created new backups and removed excess data off the archive share. 

Total: $300

 
 """ #WORKS

insideMessage(message)