class Alarm: 
    possibleTimes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    alarmLength = 0
    currentTime = 0
    
    def __init__(self, alarmLength, currentTime):
        self.alarmLength = alarmLength
        self.currentTime = currentTime
    
    #My initial thought on how to solve this problem with a list
    def calculateAlarmTime(self): 
        counter = self.alarmLength
        alarmTime = self.possibleTimes[self.currentTime]
        
        
        while counter > 0:
            alarmTime += 1
            counter -= 1
            
            if alarmTime > 23:
                alarmTime -= 24
            
        print(f'The time when the alarm goes off will be{alarmTime}. This will be calculated with the first method.')
    
    #Refined solution
    def calculateAlarmTime2(self):
        time = 0
        time = self.currentTime + self.alarmLength % 24
        
        print (f'The time when the alarm goes off will be{time}. This was calculated with the second method.')
        
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
def validateInputCurrent(value):
    if value < 0 or value > 24:
        raise InvalidInputError(f'Input must be between 0 and 24, not {value} ')
def validateInputTimer(value):
    if value < 0:
        raise InvalidInputError(f'Input must be greater than 0, not {value} ')
    
    
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

        taxTotal = self.total * self.salesTax
        print(f'The total for tax is: $' + str(round(taxTotal, 2)))

        self.total += taxTotal
        print(f'The total for the meal with tax is: $' + str(round(self.total, 2)))

        tipTotal = self.total * self.tip
        print(f'The total for the tip is: $' + str(round(tipTotal, 2)))

        self.total += tipTotal
        print(f'The total for the meal, tip, and tax is: $' + str(round(self.total, 2)))

class Main:       
    def __init__(self):
        self.mealCost = self.getMealCost()
        self.meal = MealCalc(self.mealCost)
        self.meal.calculateTotal()
        
        self.current = self.getCurrent()
        self.timer = self.getTimer()
        self.alarm = Alarm(self.timer, self.current)
        self.alarm.calculateAlarmTime()
        self.alarm.calculateAlarmTime2()
    
    def getCurrent(self):
        while True:
            try:
                current = int(input(f'What is the current time: '))
                validateInputCurrent(current)
                break
            except InvalidInputError as e:
                print(e.message)
                
        return current

    def getTimer(self):
        while True:
            try:
                timer = int(input(f'How long would you like the timer to be: '))
                validateInputTimer(timer)
                break
            except InvalidInputError as e:
                print(e.message)
                
        return timer
    
    def getMealCost(self):
        while True:
            try:
                mealCost = float(input(f'How much did your meal cost: '))
                validateInputTimer(mealCost)
                break
            except InvalidInputError as e:
                print(e.message)
                
        return mealCost

if __name__ == "__main__": 
    Main()