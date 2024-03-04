#Class containing dictionaries. Combines the dictionaries into one.
class courseDictionary:
    roomNumbers = {"CSC 101": 3004, "CSC 102": 4501, "CSC 103": 6755, "NET 110": 1244, "COM 241": 1411}
    instructors = {"CSC 101": "Haynes", "CSC 102": "Alvarado", "CSC 103": "Rich", "NET 110": "Burke", "COM 241": "Lee"}
    meetingTime = {"CSC 101": "8:00 a.m", "CSC 102": "9:00 a.m", "CSC 103": "10:00 a.m", "NET 110": "11:00 a.m", "COM 241": "1:00 p.m"}
    allClassInfo = {}
    
    def __init__(self):
        self.roomNumbers = self.roomNumbers
        self.instructors = self.instructors
        self.meetingTime = self.meetingTime
        for key in self.roomNumbers:
            self.allClassInfo[key] = [self.roomNumbers[key], self.instructors[key], self.meetingTime[key]]
            
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
def validateInput(value):
    if value < 1 or value > 6:
        raise InvalidInputError(f'Input must be greater than 0, not {value} ')
            
class Main: 
    def __init__(self):
        courseInfo = courseDictionary()
        classKeys = list(courseInfo.allClassInfo.keys())
        
        self.choice = self.menu()
        while self.choice != 6:
            
            index = self.choice -1
            key = classKeys[index]
            print(f"{key} \nRoom Number: {courseInfo.allClassInfo[key][0]}\nInstructor: {courseInfo.allClassInfo[key][1]}\nMeeting time: {courseInfo.allClassInfo[key][2]}\n")
            
            self.choice = self.menu()
        
    #Allows the user to select which class to display info.    
    def menu(self):
        print(f"Class Options")
        print(f"1. CSC 101")
        print(f"2. CSC 102")
        print(f"3. CSC 103")
        print(f"4. Net 110")
        print(f"5. COM 241")
        print(f"6. Quit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice >= 1 and choice <= 6:
                    return choice
                else:
                    raise InvalidInputError("Choice must be between 1 and 6. Choice must be the number corresponding to the desired class.")
            except InvalidInputError as e:
                print(e.message)
            except ValueError:
                print("Invalid input. Please enter a number.")
                
if __name__ == "__main__":
    Main() 