# simple creating classe
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("john", 25)
p1.myfunc()

print(p1.age)

p1.age = 35
print(p1.age)
