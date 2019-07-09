#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 09/07/19
# Purpose: To Understand How to use Regex and hopefully classes. 
#############################################################################

#############################################################################

import re

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################

#############################################################################
# Input: null
# This function changes the re compile code to find patterns. 
# Output: null
#############################################################################

class RegexQuery: 
    def __init__(self): 
        self.mobilePhoneNum = re.compile(r'\d\d\d\d \d\d\d \d\d\d')
        self.homePhoneNum = re.compile(r'\d\d\d\d \d\d\d\d')

#############################################################################
# 								Main Code. 
#############################################################################

phoneNumRegex = re.compile(r'\d\d\d\d \d\d\d \d\d\d')

query = phoneNumRegex.search("My Number is 0458 770 196")

print("Found number is " + query.group())
