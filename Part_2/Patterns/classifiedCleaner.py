#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 9/07/19
# Purpose: Redacting Classified information from NSA Documents.]
# Source: https://docs.python.org/3/howto/regex.html
#############################################################################

#############################################################################

import re as regex
import time

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################

#############################################################################
# Input: Un-redacted text
# This function redacts the text to make sure that it is safe to been shown 
# to the public. 
# Output: cleaned information.
#############################################################################

def classifiedCleaner(beforeRedacted):
	classifiedRegex = regex.compile(r'Agent (\w)\w*', regex.IGNORECASE)

	classified = classifiedRegex.match(beforeRedacted)
	
	if classified:
		x = 0
		print("Match found: ")
		while x !=3:
			print("REDACTING...")
			time.sleep(0.2)
			x += 1
		redacted = classifiedRegex.sub(r'Agent \1****', beforeRedacted)
		return redacted
		print("REDACTED.")

	else:
		return "No Classifed Information"

#############################################################################
# 								Main Code. 
#############################################################################

Uncleaned = """Agent Wells killed a lot of men. agent Jacob spoke to her
and was like damn son, why'd you do that."""

Cleaned = classifiedCleaner(Uncleaned)

print(Cleaned)