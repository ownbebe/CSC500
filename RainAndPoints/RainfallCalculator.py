class RainfallCalculator:
    yearlyTotals = []
    monthlyTotals = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, 
                     "July": 0, "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}
    totalyears = 0
    totalRain = 0
    yearRain = 0
    
    #Constructor
    def __init__(self, totalYears):
        self.totalyears = totalYears
        self.yearlyTotals = self.yearlyTotals
        self.monthlyTotals = self.monthlyTotals
        self.totalRain = self.totalRain
        self.yearRain = self.yearRain
    
    #Method for gathering input and calculating total rainfall
    #Inner loop gets input for each month of the year, outer loop calculates total for given amount of years
    def getInput(self):
        for year in range (0, self.totalyears):
            for month in range (0, 12):
                if month == 0:
                    monthName = "January"
                elif month == 1:
                    monthName = "February"
                elif month == 2:
                    monthName = "March"
                elif month == 3:
                    monthName = "April"
                elif month == 4:
                    monthName = "May"
                elif month == 5:
                    monthName = "June"
                elif month == 6:
                    monthName = "July"
                elif month == 7:
                    monthName = "August"
                elif month == 8:
                    monthName = "September"
                elif month == 9:
                    monthName = "October"
                elif month == 10:
                    monthName = "November"
                elif month == 11:
                    monthName = "December"
                
                while True:
                    try:
                        rain = float(input(f"Enter the total rain fall for {monthName} in year {year + 1}: "))
                        validateInputYears(rain)
                        break
                    except InvalidInputError as e:
                        print(e.message)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        
                self.monthlyTotals[monthName] = rain
                        
                
            self.yearRain = sum(self.monthlyTotals.values())
            self.totalRain += self.yearRain
                
        print(f"The total rainfall was {self.totalRain} inches.")
        
#validates user input
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
def validateInputYears(value):
    if value < 0:
        raise InvalidInputError(f'Input must be greater than 0, not {value} ')
                
class Main:
    def __init__(self):
        self.years = self.getYears()
        self.RainFallCalculator = RainfallCalculator(self.years)
        self.RainFallCalculator.getInput()
        
    def getYears(self):
        while True:
            try:
                years = int(input("Enter the number of years to be calculated: "))
                validateInputYears(years)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        return years
    
if __name__ == "__main__": 
    Main()
                