## create parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

## parent class object
x = Person("John", "Doe")
x.printname()

# create child class
class Student(Person):
    def __init__(self, fname, lname, year):  # create __init__() function in child class no longer inherit the parent __init__()
        # Person.__init__(self, fname, lname) # Keep inheritance of parent's __init__() function
        super().__init__(fname, lname)
        self.graduationyear = year 
    
    def welcome(self):
       print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike","Olsen",2019)
x.printname()
x.welcome()
