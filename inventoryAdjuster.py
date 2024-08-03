import DataStructure

#This page of code will be used to fetch the commands from DataStructure.py

#Prompts if Inventory is added:

decision = input("Do you want to add, give, or override the inventory?")

if decision.upper() == "ADD":
    newitem =  DataStructure.item(input("What is the item called?"),int(input("How many?")),input("Scan ASIN"))
    
    print(newitem.name, " ", newitem.code, " ", newitem.count)

if decision.upper() == "GIVE":
    DataStructure.giveItem(input("Please Scan ASIN"))
    print(DataStructure.items)

if decision.upper() == "INVENTORY":
    DataStructure.overrideInventory(input("Please scan ASIN"))




