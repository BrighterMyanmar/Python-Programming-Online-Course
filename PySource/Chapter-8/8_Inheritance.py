class Person:
    name = "Jhon Doe"
    age = 20 
    heigh = 5.11

    def detail(self):
        print(f"Name is {self.name}")
        print(f'Age is {self.age}')
        print(f'Heigh is {self.heigh}')

class Boy(Person): # Boy class inherit from Person
    pass

class Girl(Person): # Child/SubClass/derive => Girl , Parent/Super => Person
    pass

b = Boy() 
b.detail()

g = Girl()
print(g.name)