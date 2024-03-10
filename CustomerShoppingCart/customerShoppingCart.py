#class for items that will be in the shopping cart
class ItemToPurchase:
    itemName = "none"
    itemPrice = 0.00
    itemQuantity = 0
    itemDescription = "none"
    
    def __init__(self, itemName, itemPrice, itemQuantity, itemDescription):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity
        self.itemDescription = itemDescription
        
    #method for finding the total of an individual item
    def itemTotal(self):
        return self.itemPrice * self.itemQuantity
        
    #method for displaying item information
    def print_item_cost(self):
        return f'{self.itemName} {self.itemQuantity} @ ${self.itemPrice:.2f} = ${self.itemTotal():.2f}'    

#Custom exception for validating input
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
def validateInput(value):
    if value < 0:
        raise InvalidInputError(f'Input must be greater than 0, not {value} ')
def validateString(value):
    if "".__eq__(value):
        raise InvalidInputError(f'You must enter a string')

class Maintenance:
    #empty constructor
    def __init__(self):
        None
    
    #method for retrieving item information from customer
    def itemInput(self):
        while True:
            try:
                itemName = str(input("Enter the name of the item: "))
                validateString(itemName)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print(f"Invalid input type. Please try again. ")
                    
        while True:
            try:
                itemPrice = float(input("Enther the price of the item: "))
                validateInput(itemPrice)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print(f"Invalid input type. Please try again.")
                    
        while True:
            try:
                itemQuantity = int(input("Enter the quantity being purchased: "))
                validateInput(itemQuantity)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print(f"Invalid input type. Please try again.")
                
        while True:
            try:
                itemDescription = str(input("Enter the description of the item: "))
                validateString(itemDescription)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print(f"Invalid input type. Please try again. ")
        
        
        
        item = ItemToPurchase(itemName, itemPrice, itemQuantity, itemDescription)
        
        return item
    
    #method that displays item information. No longer needed
    def display(self):
        print(f'Item 1')
        item1 = self.itemInput()
        
        print(f'Item 2')
        item2 = self.itemInput()
        
        totalCost = item1.itemTotal() + item2.itemTotal()
        print(f'TOTAL COST \n{item1.print_item_cost()} \n{item2.print_item_cost()}\n Total: ${totalCost:.2f}')

#Class that will hold and maintain information for the shopping cart throughout execution        
class ShoppingCart:
    customerName = "none"
    customerDate = "January 1, 2020"
    
    #constructor
    def __init__(self, customerName, customerDate):
        self.customerName = customerName
        self.customerDate = customerDate
        self.cartItems: list[ItemToPurchase] = []
        
    #helper method for finding an item within the list
    def findItem(self, itemName):
        for item in self.cartItems:
            if item.itemName.lower() == str(itemName).lower():
                return self.cartItems.index(item)
            
        return -1
    
    #method to add an item to the list   
    def addItem(self, item):
        self.cartItems.append(item)
        
    #method to remove an item from list
    def removeItem(self, itemName):
            index = self.findItem(itemName)
            if index == -1:
                print(f"Item not found in cart. Nothing removed.")
            else:
                self.cartItems.pop(index)
            
    #method to update an item within the list
    def modifyItems(self, item):
        index = self.findItem(item)
        maintain = Maintenance()
        if index == -1:
            print(f"Item not found in cart. Nothing modified")
        else:
            while True:
                try:
                    newQuantity = int(input("Enter the new quantity for your item: "))
                    validateInput(newQuantity)
                    break
                except InvalidInputError as e:
                    print(e.message)
                except ValueError:
                    print(f"Invalid value error")
            self.cartItems[index].itemQuantity = newQuantity
    
    #method for getting length of list
    def getNumInCart(self):
        itemsInCart = len(self.cartItems)
        return itemsInCart
    
    #method for finding total of items in list
    def getCostOfCart(self):
        totalCost = 0
        for item in self.cartItems:
            totalCost += item.itemTotal()
        
        return totalCost
    
    #method for printing item information within the list
    def printTotal(self):
        print(f"{self.customerName}'s Shopping Cart - {self.customerDate}")
        for item in self.cartItems:
                print(f"{item.print_item_cost()}")
                
        print(f"Total: ${self.getCostOfCart():.2f}\n")
        
    #method for printing the item name for each item in the list
    def printDescriptions(self):
        print(f"{self.customerName}'s Shopping Cart - {self.customerDate}")
        if(len(self.cartItems) == 0):
            print(f"There are no items in the cart.")
        for item in self.cartItems:
            print(f"{item.itemName}: {item.itemDescription}")
 
#Where the program will be started              
class Main: 
    def __init__(self):
        self.maintain = Maintenance()
        self.customerName, self.date = self.getCustomerInfo() 
        self.shoppingCart = ShoppingCart(self.customerName, self.date)
        
        self.choice = self.menu(self.shoppingCart)
        while self.choice != 'q':
            if self.choice == 'a':
                self.item = self.maintain.itemInput()
                self.shoppingCart.addItem(self.item)
            elif self.choice == 'r':
                self.itemName = self.getName()
                self.shoppingCart.removeItem(self.itemName)
            elif self.choice == 'c':
                self.itemName = self.getName()
                self.shoppingCart.modifyItems(self.itemName)
            elif self.choice == 'i':
                self.shoppingCart.printDescriptions()
            elif self.choice == 'o':
                self.shoppingCart.printTotal()
                
            self.choice = self.menu(self.shoppingCart)
                
    #Allows user to decide what will happen next in the program        
    def menu(self, shoppingCart):
        print(f"Menu")
        print(f"Enter corresponding letter")
        print(f"a. Add item to cart")
        print(f"r. Remove item from cart")
        print(f"c. Modify existing item in cart")
        print(f"i. Output items' description")
        print(f"o. Output shopping cart")
        print(f"q. Quit")

        while True:
            try:
                choice = str(input("Enter your choice: ")).lower()
                if choice == 'a' or 'r' or 'c' or 'i' or 'o' or 'q':
                    return choice
                else:
                    raise InvalidInputError(f"Choice must be be the letter corresponding to a given option.")
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print("Invalid input. Please enter a valid letter.")
                
    #helper method for retrireving item name
    def getName(self):
        while True:
            try:
                itemName = str(input("Enter the name of the item: "))
                validateString(itemName)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print(f"Invalid input type. Try again.")
                    
        return itemName
    
    #helper method for getting customer information
    def getCustomerInfo(self):
        while True:
            try:
                customerName = str(input("Enter your name: "))
                validateString(customerName)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print(f"Invalid input type. Try again.")
        
        while True:
            try:
                date = str(input("Enter the date: "))
                validateString(date)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print(f"Invalid input type. Try again.")
                    
        return customerName, date
        
        
        
        
if __name__ == "__main__":
    Main()       