#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 11/07/19
# Purpose: To find whether a phone number is an Australian Phone-Number
# but we are using the verbose mode and the different flag options inside of
# re, instead of using conditions. 
#############################################################################

#############################################################################

import re as regex

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################

#############################################################################
# Input: rawText
# This function takes in raw text and extracts phone numbers. 
# Output: the found numbers. 
#############################################################################

def isAussieNumber(rawText):

	AUphoneRegex = regex.compile(r"""(
	[+]61\s)+
	(\s|-|\.)*
	(\d{3})+
	(\s|-|\.|)*
	(\d{3})+
	(\s|-|\.)*
	(\d{3})+

	""", regex.VERBOSE)

	foundNumbers = AUphoneRegex.findall(rawText)

	return foundNumbers


#############################################################################
# 								Main Code. 
#############################################################################

rawText = "+61 424 121 121, +61248248438 0423 342 234"

AussieNumbers = isAussieNumber(rawText)
print(AussieNumbers)