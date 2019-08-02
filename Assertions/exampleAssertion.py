#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: DATE
# Purpose: FILL ME ...  PLEASE! 
#############################################################################

#############################################################################

import traceback

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################
class otherClass:
    def __init__(self):
    	self.x = 10
    	self.str = "HELLO!"

    def getData(self):
        print("{0}+{1}j".format(self.x,self.x))


#############################################################################
# Input: input
# This function DOES
# Output: input
#############################################################################
def spam():
	bacon()


def bacon():
	try:
		raise Expection("OMG ERROR?")
	except:
		errorFile = open('errorInfo.txt', 'w')
		errorFile.write(traceback.format_exc())
		errorFile.close()
		print('The traceback info was written to errorInfo.txt.')


def ErrorException():
	while True:
		try:
			x = int(input("Enter a valid number: "))
			break
		except ValueError:
			print("Invalid Number, please try again.")
		except NameError:
			pass
def assertCheck():
	assert "red" in dog, "Neither "

#############################################################################
# 								Main Code. 
#############################################################################


spam()
ErrorException()
PythonExample()