#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 25/07/19
# Purpose: To Understand Classes Better. 
#############################################################################

#############################################################################

import random as r

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################
class eSportsPlayer:
    def __init__(self,name, age, team):
    	self.name = name
    	self.age = age
    	self.team = team


    def getData(self):
        print("Name: %s\n Age: %d\n Team: %s\n" % (self.name, self.age, self.team))


#############################################################################
# Input: input
# This function DOES
# Output: input
#############################################################################

def aFunFuction(input):
	extra = input + 1
	return input, extra

#############################################################################
# 								Main Code. 
#############################################################################

Jayden = eSportsPlayer("Jayden", 18, "UTS")
Jayden.Dad = eSportsPlayer.Dad("Ray", 55)
Jayden.getData()


print(Jayden.name)