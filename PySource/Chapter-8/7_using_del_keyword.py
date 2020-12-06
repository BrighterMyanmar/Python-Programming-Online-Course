class Main :
    def __init__(self,name):
        self.name = name

    def showName(self):
        print(f'Name is {self.name}')
    
    def outPut(self):
        print("I am output")

m1 = Main("Mg Mg") # self.name "Mg Mg"
del m1.name # del self.name # attribute
del m1
m1.outPut()
m1.showName() # Name is "Mg Mg"