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