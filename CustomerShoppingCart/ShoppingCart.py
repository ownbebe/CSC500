from ItemToPurchase import ItemToPurchase
from Main import Maintenance

class ShoppingCart:
    customerName = "none"
    customerDate = "January 1, 2020"
    
    def __init__(self, customerName, customerDate):
        self.customerName = customerName
        self.customerDate = customerDate
        self.cartItems: list[ItemToPurchase] = []
        
    def findItem(self, itemName):
        for item in self.cartItems:
            if item.itemName == itemName:
                return self.cartItems.index(item)
            
        return -1
    

        
    def addItem(self, item):
        self.cartItems.append(item)
        
    def removeItem(self, itemName):
            index = self.findItem(itemName)
            if index == -1:
                print(f"Item not found in cart. Nothing removed.")
            else:
                self.cartItems.pop(index)
            
    def modifyItems(self, item):
        index = self.findItem(item)
        maintain = Maintenance()
        if index == -1:
            print(f"Item not found in cart. Nothing modified")
        else:
            modifiedItem = maintain.itemInput()
            self.cartItems[index] = modifiedItem
    
    def getNumInCart(self):
        itemsInCart = len(self.cartItems)
        return itemsInCart
    
    def getCostOfCart(self):
        totalCost = 0
        for item in self.cartItems:
            totalCost += item.itemTotal()
        
        return totalCost
    
    def printTotal(self):
        print(f"{self.customerName}'s Shopping Cart - {self.customerDate}")
        for item in self.cartItems:
                print(f"{item.print_item_cost()}")
                
        print(f"Total: ${self.getCostOfCart():.2f}\n")
        
    def printDescriptions(self):
        print(f"{self.customerName}'s Shopping Cart - {self.customerDate}")
        for item in self.cartItems:
            print(f"{item.itemName}")
