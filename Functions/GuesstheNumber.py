###############################################################################
# Author: Jayden Lee
# Date: 27/06/19
# Purpose: Simple number guesser game that also demonstraits a lot of good
# Python coding practice and random things to refreshes my memory on Python 
# cause I'm disabled. 

###############################################################################


import random as r


minRange = int(input("Please give me a minimum number: "))
maxRange = int(input("Please give me a maximum number: "))
genInt = r.randrange(minRange, maxRange)
Correct = 0

def Guesser(minRange, maxRange, Debug):
	# Start of Debug
	if Debug == 1:
		print(str(genInt))
	# End of Debug
	Guess = int(input("Please enter a number between " + str(minRange) 
	+ " and " + str(maxRange) + ": "))
	if Guess < genInt:
		print("Your guess was a little too low. ")
		return 0
	elif Guess > genInt:
		print("Your guess was a little too high. ")
		return 0
	elif Guess == genInt:
		print("Correct! ")
		return 1



while Correct != 1:
	Correct = Guesser(minRange, maxRange, 0)
