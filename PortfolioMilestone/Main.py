import ItemToPurchase as ITP 

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
    def __init__(self) -> None:
        pass
    
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
        
        
        
        item = ITP.ItemToPurchase(itemName, itemPrice, itemQuantity)
        
        return item
    
    def display(self):
        print(f'Item 1')
        item1 = self.itemInput()
        
        print(f'Item 2')
        item2 = self.itemInput()
        
        totalCost = item1.itemTotal() + item2.itemTotal()
        print(f'TOTAL COST \n{item1.print_item_cost()} \n{item2.print_item_cost()}\nTotal: ${totalCost:.2f}')
        
class Main: 
    def __init__(self):
        self.Maintenance = Maintenance()
        self.Maintenance.display()
        
        
        
if __name__ == "__main__":
    Main()       