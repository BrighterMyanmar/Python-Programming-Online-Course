class Main:
    name=age=heigh=""
    def __init__(self,name,age,heigh): # build-in method
        self.name = name
        self.age = age
        self.heigh = heigh
        print("I am initilization method!")

    def show(self,result):
        print(f'Name is {self.name} age is {self.age} heigh is {self.heigh} return {result}')

m1 = Main(name="Mg Mg",age=20,heigh=5.11)  # initialization method is invoked when instantitate Class
m1.show("Hey")
