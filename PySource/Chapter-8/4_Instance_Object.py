class Main : # blueprint
    name = "Mg Mg"
    age = 20


m1 = Main() # #x123123 => Main class instance Object
m2 = Main() # #x123124 => 

m1.name = "Aung Aung"
m2.name = "Tun Tun"
print(m1.name)
print(m2.name)

"""
    to use properties or methods of a class, create its instance object

    #x123123 => class Main : # blueprint
                    name = "Mg Mg"
                    age = 20
    #x123124 => class Main : # blueprint
                    name = "Mg Mg"
                    age = 20
"""
