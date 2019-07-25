###############################################################################
# Author: Jayden Lee
# Date: 27/06/19
# Purpose: Simple list concatecation and looping example.

###############################################################################


maxPosition = int(input("Please enter the size of the list: "))
theList = []

for loopPostion in range(maxPosition):
	name = input("Please enter the " + str(loopPostion)
	 + "nth value for the list: ")
	theList = theList + [name]
del theList[maxPosition-1]

theList.sort()
theList.append("OwO")
print("The Stored List is: ")
for i in range(maxPosition):
	print("    " + theList[i])




