class MultorDivide:
    num1 = 0
    num2 = 0
    multAnswer = 0
    divideAnswer = 0

    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y
        

    def calculate(self):
        self.multAnswer = self.num1 * self.num2 
        self.divideAnswer = self.num1 / self.num2
        print("The numbers added equlas " + str(self.multAnswer))
        print("The numbers subtracted equals " + str(self.divideAnswer))
       
input1 = float(input("Enter your first number: "))
input2 = float(input("Enter your second number: "))

obj = MultorDivide(input1, input2)
obj.calculate()