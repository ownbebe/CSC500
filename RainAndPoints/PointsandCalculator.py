class RainfallCalculator:
    yearlyTotals = []
    monthlyTotals = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, 
                     "July": 0, "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}
    totalyears = 0
    totalRain = 0
    yearRain = 0
    
    def __init__(self, totalYears):
        self.totalyears = totalYears
        self.yearlyTotals = self.yearlyTotals
        self.monthlyTotals = self.monthlyTotals
        self.totalRain = self.totalRain
        self.yearRain = self.yearRain
    
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
        
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
def validateInputYears(value):
    if value < 0:
        raise InvalidInputError(f'Input must be greater than 0, not {value} ')
    
class BookStorePoints:
    points = 0
    booksPurchased = 0
    
    def __init__(self, booksPurchased):
        self. points = self.points
        self.booksPurchased = booksPurchased
        
    def calculate(self):
        if(self.booksPurchased == 0):
            self.points = 0
            
        elif(self.booksPurchased >= 8):
            self.points = 60
            
        else:
            multiplier = 2.5
            counter = 1
            total = 0 
            
            for x in range(1, self.booksPurchased + 1):
                total += multiplier
                if(x % 2 == 0):
                    counter += 1
                    multiplier = 2.5 * counter
                
            self.points = total
        print(f"Your points total is {self.points}")
                
class Main:
    def __init__(self):
        self.choice = self.menu()
        while self.choice != 3:
            if self.choice == 1:
                self.years = self.getYears()
                self.RainFallCalculator = RainfallCalculator(self.years)
                self.RainFallCalculator.getInput()
            elif self.choice == 2:
                self.books = self.getBooks()
                self.pointsCalculator = BookStorePoints(self.books)
                self.pointsCalculator.calculate()
            self.choice = self.menu()
        
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
    
    def getBooks(self):
        while True:
            try:
                books = int(input("Enter the number of books purchased: "))
                validateInputYears(books)
                break
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print("Invalid input. Please enter a number.")
        return books
        
    def menu(self):
        print(f"Enter your choice")
        print(f"1. Calculate rainfall")
        print(f"2. Calculate bookstore points")
        print(f"3. Exit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice >= 1 and choice <= 3:
                    return choice
                else:
                    raise InvalidInputError("Choice must be between 1 and 3, inclusive.")
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print("Invalid input. Please enter a number.")
    
if __name__ == "__main__": 
    Main()