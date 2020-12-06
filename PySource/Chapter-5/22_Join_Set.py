names1 = {"Mg Mg","Aung Aung"}
names2 = {"Aung Aung","Tun Tun","Su Su"}

# names = names1.union(names2) # yield new value
# names1.update(names2)

# x = names1.intersection(names2) # get value appear in both set
# z = names1.symmetric_difference(names2) # get values not appear in both set

# names1.intersection_update(names2)

# names1.symmetric_difference_update(names2)
dif = names1.difference(names2)
print(dif)

"""
    union ->
    update -> 
    intersection -> 
    intersection_update -> 
    symmetric_difference <=> difference -> 
    symmetric_difference_update->
"""