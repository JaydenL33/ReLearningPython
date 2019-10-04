#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au)
# Date: 1/10/2019
# Purpose: In order to vote on the predicited values, I've used a vote. 
# Meaning that if the the values occur more then 3 times, then it will be the
# final voted value. For 31250 Introduction into Data Analytics.

""" 
README!!!!!!!!!!!!!!!!!!


If you want to use this program, you will need to extract the prediction 
values from your classifers and the corrosponding QUOTE ID and have it
as the only too columns. You can do this by using the column filter in
Knime. From this, you can use this as a decision matrix, which weights
each value equally. WARNING: If one of your classifers such then please
DO NOT use it.

""" 

#############################################################################

#############################################################################

import csv

#############################################################################

#############################################################################
# 							Function and Class Def.
#############################################################################

#############################################################################
# Input: Tables(The List of Tables), 
# n (Being the of tables gone through already)
# This function DOES
# Output: NULL
#############################################################################

def CSVLoad(tables, name, n):
	with open(name[n] + '.csv', mode='r') as Voting:
		read_data = csv.reader(Voting, delimiter=' ', quotechar='|')
		read_data = list(read_data)
		#print(read_data)
		#print(len(read_data))

	for i in (len(read_data)-1):
		tables[i+1[n]] = read_data[i+1[0]]
		tables[i+1[n+1]] = read_data[i+1[1]]

#############################################################################
# Input: Tables(The extracted value as whether or not it was 1 or 0 for each
# outputted result from Knime.
# finalTable (The final table to write too.)
# This function returns a list of weather a majority of the results were 1 
# or 0.
# Output: NULL
#############################################################################

def Voting(tables, finalTable, Outputs):

	for i in range(len(tables)):
		for l in range(len(tables[i])):
			entrySum += tables[i[l]]
		if entrySum >= NumOfOutput/2:
			finalTable[i] = 1
		else: 
			finalTable[i] = 0

#############################################################################
# 								Main Code. 
#############################################################################

finalTable = []
tables = []
tables[0[0]] = "Quote_ID"
tables[0[1]] = "QuoteConversion_Flag"
names = []
name = []

NumOfOutput = 5

i = 0
for i in range(NumOfOutput):
	
	input_Name = str(input("What is the name of the CSV? "))
	name.append(input_Name)
	# print(str(name[i]))
	
	CSVLoad(tables, name, i)

#Voting(tables, finalTable, NumOfOutput)
