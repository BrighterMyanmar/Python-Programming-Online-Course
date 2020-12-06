class Animal :
    def __init__(self):
        print("I am Parent")
    
    def show(self):
        print("I am Parent's Show Method")

class Dog(Animal):
    def __init__(self):
        print("I am Child")
        super().__init__()
    def show(self):
        super().show()
        print("I am Child's Show Method!")
d = Dog()
d.show()


"""
class Animal:
    sound = "Animal Sound"
    def makeSound(self):
        print(f'Making Noise {self.sound} {self.sound} {self.sound}')

class Dog(Animal):
    pass



class Lion(Animal):
    def makeSound(self):
        self.sound = "Roar"
        print(f'Making Noise {self.sound} {self.sound} {self.sound}')


lion = Lion() 
lion.sound = "Roar"
lion.makeSound()

"""