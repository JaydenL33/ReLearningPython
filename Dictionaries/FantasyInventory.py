###############################################################################
# Author: Jayden Lee
# Date: 28/06/19
# Purpose: Data Dictionary to print a simple inventory. 

###############################################################################


Inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory():
	count = 0
	print("Inventory: ")
	for i in Inventory:
		print(str(Inventory[i]) , str(i))
		count = count + int(Inventory[i])
	print("Number of items in inventory is: " + str(count))

displayInventory()