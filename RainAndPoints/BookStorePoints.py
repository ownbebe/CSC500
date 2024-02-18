class BookStorePoints:
    points = 0
    booksPurchased = 0
    
    def __init__(self, booksPurchased):
        self.points = self.points
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
        print(self.points)
        
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
            
        return books
        
if __name__ == "__main__": 
    Main()