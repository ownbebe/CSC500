class AddOrSub:
    num1 = 0
    num2 = 0
    addAnswer = 0
    subAnswer = 0

    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y
        

    def calculate(self):
        self.addAnswer = self.num1 + self.num2 
        self.subAnswer = self.num1 - self.num2
        print("The numbers added equlas " + str(self.addAnswer))
        print("The numbers subtracted equals " + str(self.subAnswer))
       
input1 = float(input("Enter your first number: "))
input2 = float(input("Enter your second number: "))

obj = AddOrSub(input1, input2)
obj.calculate()