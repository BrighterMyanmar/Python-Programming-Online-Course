class Main:  # blueprint
    name = "Mg Mg"

    def change(self):
        print(self.name)


m1 = Main()  # Main().name
m1.name = "Aung Aung"
m1.change()

m2 = Main() 
m2.name = "Tun Tun"
m2.change()

"""
    to use properties or methods of a class, create its instance object

    m1 => #x123123 => class Main:  # blueprint
                        name = "Mg Mg"
                        def change(self):
                            print(self.name)
    m2 => #x123124 => class Main:  # blueprint
                        name = "Mg Mg"
                        def change(self):
                            print(self.name)
"""