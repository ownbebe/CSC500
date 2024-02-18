class BookStorePoints:
    points = 0
    booksPurchased = 0
    
    #Constructor
    def __init__(self, booksPurchased):
        self.points = self.points
        self.booksPurchased = booksPurchased
        
    #Method for calculating total points
    def calculate(self):
        if(self.booksPurchased == 0):
            self.points = 0
            
        elif(self.booksPurchased >= 8):
            self.points = 60
            
        else:
            onGoingPoints = 2.5
            multiplier = 1
            total = 0 
            
            #Every even number increases the points being added to the total by 2.5
            #0-2 books = 2.5, 3-4 = 5, 5-6 = 7.5, 7 = 10
            for x in range(1, self.booksPurchased + 1):
                total += onGoingPoints
                if(x % 2 == 0):
                    multiplier += 1
                    onGoingPoints = 2.5 * multiplier
                
            self.points = total
        print(f"Your points total is {self.points}")
        
#validates input
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
def validateInputYears(value):
    if value < 0:
        raise InvalidInputError(f'Input must be greater than 0, not {value} ')
        
class Main: 
    def __init__(self):
        self.books = self.getBooks()
        self.pointsCalculator = BookStorePoints(self.books)
        self.pointsCalculator.calculate()
        
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
        
if __name__ == "__main__": 
    Main()