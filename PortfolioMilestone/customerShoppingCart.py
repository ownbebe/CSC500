class ItemToPurchase:
    itemName = "none"
    itemPrice = 0.00
    itemQuantity = 0
    
    def __init__(self, itemName, itemPrice, itemQuantity):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity
        
    def itemTotal(self):
        return self.itemPrice * self.itemQuantity
        
    def print_item_cost(self):
        return f'{self.itemName} {self.itemQuantity} @ ${self.itemPrice:.2f} = ${self.itemTotal():.2f}'    

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
    def __init__(self):
        None
    
    def itemInput(self):
        while True:
            try:
                itemName = str(input("Enter the name of the item: "))
                validateString(itemName)
                break
            except InvalidInputError as e:
                    print(e.message)
                    
        while True:
            try:
                itemPrice = float(input("Enther the price of the item: "))
                validateInput(itemPrice)
                break
            except InvalidInputError as e:
                    print(e.message)
                    
        while True:
            try:
                itemQuantity = int(input("Enter the quantity being purchased: "))
                validateInput(itemQuantity)
                break
            except InvalidInputError as e:
                    print(e.message)
        
        
        
        item = ItemToPurchase(itemName, itemPrice, itemQuantity)
        
        return item
    
    def display(self):
        print(f'Item 1')
        item1 = self.itemInput()
        
        print(f'Item 2')
        item2 = self.itemInput()
        
        totalCost = item1.itemTotal() + item2.itemTotal()
        print(f'TOTAL COST \n{item1.print_item_cost()} \n{item2.print_item_cost()}\n Total: ${totalCost:.2f}')
        
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



        
        
class Main: 
    def __init__(self):
        self.maintain = Maintenance()
        self.customerName, self.date = self.getCustomerInfo() 
        self.shoppingCart = ShoppingCart(self.customerName, self.date)
        
        self.choice = self.menu(self.shoppingCart)
        while self.choice != 6:
            if self.choice == 1:
                self.item = self.maintain.itemInput()
                self.shoppingCart.addItem(self.item)
            elif self.choice == 2:
                self.itemName = self.getName()
                self.shoppingCart.removeItem(self.itemName)
            elif self.choice == 3:
                self.itemName = self.getName()
                self.shoppingCart.modifyItems(self.itemName)
            elif self.choice == 4:
                self.shoppingCart.printDescriptions()
            elif self.choice == 5:
                self.shoppingCart.printTotal()
                
            self.choice = self.menu(self.shoppingCart)
                
                
                
        
    def menu(self, shoppingCart):
        print(f"Menu")
        print(f"1. Add item to cart")
        print(f"2. Remove item from cart")
        print(f"3. Modify existing item in cart")
        print(f"4. Output items' description")
        print(f"5. Output shopping cart")
        print(f"6. Quit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice >= 1 and choice <= 6:
                    return choice
                else:
                    raise InvalidInputError("Choice must be between 1 and 3.")
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print("Invalid input. Please enter a number.")
                
    def getName(self):
        while True:
            try:
                itemName = str(input("Enter the name of the item: "))
                validateString(itemName)
                break
            except InvalidInputError as e:
                    print(e.message)
                    
        return itemName
    
    def getCustomerInfo(self):
        while True:
            try:
                customerName = str(input("Enter your name: "))
                validateString(customerName)
                break
            except InvalidInputError as e:
                    print(e.message)
        
        while True:
            try:
                date = str(input("Enter the date: "))
                validateString(date)
                break
            except InvalidInputError as e:
                    print(e.message)
                    
        return customerName, date
        
        
        
        
if __name__ == "__main__":
    Main()       