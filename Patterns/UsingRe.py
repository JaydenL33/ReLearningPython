#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 09/07/19
# Purpose: To Understand How to use Regex.
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



#############################################################################
# 								Main Code. 
#############################################################################


# Adding brackets will just introduce groups.

query = phoneNumRegex.search("My Number is 0458 770 196")

print("Found number is " + query.group(0))
print("All together is " + query.group(0))
print("1st is " + query.group(1))

first,second,third = query.groups(0)
print(first, second, third)
