
items = []
#used to add new items to inventory
def addStuff(barcode):
    exist = findItem(barcode)
    if exist == False:
        newThing = item(input("What is the item"), input("How Many?"), input("Scan Barcode"))
        items.append(newThing)
#This method is used to give an associate a gift
def giveItem(itemUPC):
    itemExist = findItem(itemUPC)
    if itemExist == True:
        AAid = input("Who do you want to give this to?")
        #Here I would put in the code to add AA Transaction to the Ledger
        item.quantity = item.quantity - 1
    else:
        print("Item is not in inventory")
#This method is used to find whether an item is already in the list
def findItem(itemUPC):
    itemPlace = 0
    itemExist = False
    for thing in items:
        if itemUPC == item.upc:
            return item
        else:
            itemPlace = itemPlace + 1
    return False
#This method will be used to override the inventory count
def overrideInventory(itemUPC):
   if findItem(itemUPC) == False:
       print("Item not in inventory. Please add to Inventory")
       return None
   else: 
       item.quantity = int(input("What should be the actual number?"))
       



class item: 
    name = None
    quantity = 0
    upc = 0

    def __init__ (self,name, count, code) : 
        self.name = name
        self.count = count
        self.code = code

    def addItem(thename, count, code):
        name = thename
        quantity = count
        upc = code
        items.append()











