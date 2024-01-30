class Alarm: 
    possibleTimes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    alarmLength = 0
    currentTime = 0
    
    def __init__(self, alarmLength, currentTime):
        self.alarmLength = alarmLength
        self.currentTime = currentTime
        
    def calculateAlarmTime(self): 
        counter = self.alarmLength
        iterator = 0
        alarmTime = self.possibleTimes[self.currentTime]
        if counter < 24:
            iterator += 1
        
        while counter > 0:
            if alarmTime == 23:
                alarmTime -= 24
                iterator = 0
            alarmTime = self.possibleTimes[iterator + self.currentTime]
            iterator += 1
            counter -= 1
            
        print(alarmTime)
    
    def calculateAlarmTime2(self):
        time = 0
        time = self.currentTime + self.alarmLength % 24
        
        print (time)
        
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
def validateInputCurrent(value):
    if value < 0 or value > 24:
        raise InvalidInputError(f'Input must be between 0 and 24, not {value} ')
def validateInputTimer(value):
    if value < 0:
        raise InvalidInputError(f'Input must be greater than 0, not {value} ')

class Main:       
    def __init__(self):
        self.current = self.getCurrent()
        self.timer = self.getTimer()
        self.alarm = Alarm(self.timer, self.current)
        self.alarm.calculateAlarmTime()
        self.alarm.calculateAlarmTime2()
    
    def getCurrent(self):
        while True:
            try:
                current = int(input('What is the current time: '))
                validateInputCurrent(current)
                break
            except InvalidInputError as e:
                print(e.message)
                
        return current

    def getTimer(self):
        while True:
            try:
                timer = int(input('How long would you like the timer to be: '))
                validateInputTimer(timer)
                break
            except InvalidInputError as e:
                print(e.message)
                
        return timer

if __name__ == "__main__": 
    Main()