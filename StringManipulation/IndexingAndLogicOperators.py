#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 07/07/19
# Purpose: Indexing and .upper and .lower.  

#############################################################################

# Function List.

#############################################################################


#############################################################################
# Input: point and string
# This function takes a point and a string prints it. 
# Output: null
#############################################################################

def Indexer(point, string):
	print(string[point])

#############################################################################
# Main Call. 
#############################################################################
a = True
string = input("Enter a string: ")
point = int(input("Enter a point for the string: "))



while "bob" not in string.lower() and string.isalpha():
	Indexer(point, string)
	string = input("Enter a string: ")
	point = int(input("Enter a point for the string: "))

print("We found bob!")

if a or a == True:
	print("TEST DEBUG")