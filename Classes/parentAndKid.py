#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 25/07/19
# Purpose: Literal genetic classes. 
# Source: https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
#############################################################################

#############################################################################

import random as r

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################
class parent:
    def __init__(self, f_name, l_name, eye_colour):
    	self.name = f_name
    	self.last_name = l_name
    	self.eye_colour = eye_colour


class child(parent):
	def __init__(self, f_name, eye_colour)
	self.name = f_name
	self.eye_colour = eye_colour


#############################################################################
# 								Main Code. 
#############################################################################

John = parent("John","Doe", "Blue")

Steve = child()

