#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 9/07/19
# Purpose: Redacting Classified information from NSA Documents.
#############################################################################

#############################################################################

import re as regex

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
	classifiedRegex = regex.compile(r'Agent \w+', )

	classfied = classifiedRegex.match("")
	if classfied:
    	print('Match found: ', m.group())
	else:
    	return "No Classifed Information"

#############################################################################
# 								Main Code. 
#############################################################################