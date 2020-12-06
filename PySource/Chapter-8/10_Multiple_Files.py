#help.py
name = "Mg Mg"
age = 20

def outPut():
    print(f"Name is {name} and age is {age}")

class Help:
    def answer(self):
        print("Answer Method from help.py")
#best.py
class Best:
    def show(self):
        print("Show method from Best class")

# app.py
from help import *
from best import Best as b

print(name)
print(age)
outPut()

help = Help()
help.answer()

class Main(b):
    pass

m1 = Main() 
m1.show()