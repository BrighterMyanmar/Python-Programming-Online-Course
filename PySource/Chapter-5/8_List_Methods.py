names = list(("Mg Mg","Aung Aung","Tun Tun","Su Su","Mg Mg"))

print(names.count("Mg Mg"))
names[1] = "Bo Kay" # update index 1 to "Bo Kay"
susuInd = names.index("Su Su");
names[susuInd] = "Mya Mya"

bol = 'Aung Aung' in names
print(f'Tun Tun is in names list is {bol}')

del names[names.index("Tun Tun")] # del names[2]

# del names
# names.clear()

print(names)
deletedName = names.pop(1) # if no index parameter will delete last index
print(deletedName)
print(names)

"""
    List Methods 
        -> update => Change List Value in given index
        -> in  => find searching value in list
        -> del => del list[ind]; del list
        -> clear => empty list[]
        -> pop  => without index => delete last index, with index, delete indexed element
        -> count => find times of occourance of given object
"""