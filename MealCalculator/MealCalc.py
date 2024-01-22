class MealCalc:
    total = 0
    charge = 0
    tip = 0.18
    salesTax = 0.07

    def __init__(self, charge):
        self.charge = charge

    def calculateTotal(self):
        tipTotal = 0
        taxTotal = 0
        self.total = (self.total + self.charge)
        print(self.total)

        taxTotal = self.total * self.salesTax
        print(round(taxTotal, 2))

        self.total += taxTotal
        print(round(self.total, 2))

        tipTotal = self.total * self.tip
        print(round(tipTotal, 2))

        self.total += tipTotal
        print(round(self.total, 2))


mealCost = float(input("Enter the total for the meal: "))
myObj = MealCalc(mealCost)
myObj.calculateTotal()

