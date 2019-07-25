###############################################################################
# Author: Jayden Lee
# Date: 28/06/19
# Purpose: Tick-Tack-Toe with Dictionaries and mucking around with functions.
# Doesn't actually do anything but shows how dictionaries operate and the 
# setdefault option. 

###############################################################################

import time
import os
import pprint

os.system("clear")

theBoard = {"top-L": "X", "top-M": "O", "top-R": "X",
			"mid-L": "O", "mid-M": "X", "mid-R": "O",
			"bot-L": "O", "bot-M": "O", "bot-R": "X"}

print(theBoard.keys())
print(theBoard.values())

def clearBoard():
	for key in theBoard:
		theBoard[key] = ""
		print("For Position " + str(key) + " the value is " +  
		str(theBoard[key]) + ".")
	theBoard.setdefault("Reset", "1")


clearBoard()
print(theBoard.keys())
print(theBoard.values())
clearBoard()
print(theBoard.keys())
print(theBoard.values())	

print("###############################################################################")
pprint.pprint(theBoard)