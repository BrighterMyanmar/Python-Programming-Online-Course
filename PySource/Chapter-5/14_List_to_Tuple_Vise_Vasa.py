names = ("Mg Mg","Aung Aung") # immutable Tuple
namesList = list(names) # list
namesList.append("Tun Tun") # list got 3 element
names = tuple(namesList) # lit to Tuple
print(names)

"""
    namesTuple = ("Mg Mg","Aung Aung")  # namesTuple => type => Tuple

    print(type(namesTuple))

    namesList = list(namesTuple) # Cast Tuple to List, namesList => type => List

    print(type(namesList))

    nT = tuple(namesList)  # nT => type => Tuple

    print(type(nT))

    namesTuple => namesList => nT

"""