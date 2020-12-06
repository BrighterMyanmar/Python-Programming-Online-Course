name = "MgMg,AungAung,#TunTun,SuSu,NuNu,MyaMya"


names = name.split(" ") # ["MgMg","AungAung","TunTun","SuSu"] => List
names = name.split(",",2)
names = name.split("to")
names = name.split("#")
# names = name.split(" ",3)

print(len(names))
print(type(names))
print(names)
