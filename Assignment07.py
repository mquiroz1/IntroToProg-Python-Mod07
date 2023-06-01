# ------------------------------------------------- #
# Title: Assignment 7
# Description: A simple program to store gym equipment data in a binary file
# ChangeLog: (Who, When, What)
# Marita Quiroz,<5.31.2023>,Created Script
# ------------------------------------------------- #

# Import pickle module
import pickle

# Data -------------------------------------------- #

strFileName = 'EquipInventory.dat'
eName = input("Enter equipment name: ")
# Specify exception type
# Ask user for quantity
try:
    intQty = int(input("Enter quantity: "))
    lstEquipment = [eName, intQty]
# If input is not a valid number (ValueError),
# message will be displayed back to user
except ValueError:
    print("That was not a valid quantity!")
    # Exit program
    exit()


# Processing -------------------------------------- #

# Open Equipment Inventory binary file in write mode
# If the file doesn't exist, one will be created
objFile = open("EquipInventory.dat", "wb")
# Use pickle.dump to write the object to file
pickle.dump(lstEquipment, objFile)
# Close file
objFile.close()

# Open Equipment Inventory binary file in read mode
objFile = open("EquipInventory.dat", "rb")
# Use pickle.load to load row of data
objFileData = pickle.load(objFile)
# Close file
objFile.close()
# Print current contents of file
print("Current file: ")
print(objFileData)

