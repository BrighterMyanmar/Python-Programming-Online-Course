names = ("Mg Mg","Aung Aung","Tun Tun","Su Su")
para = """Lorem Ipsum has been the industry's standard dummy 
text ever since the 1500s, when an unknown printer took a galley of 
type and scrambled it to make a type specimen book
"""
print(type(names))
names = iter(names)
print(type(names))
print(names.__next__())
print(names.__next__())
print(names.__next__())
print(names.__next__())

para = iter(para)
print(para.__next__())
print(para.__next__())
print(para.__next__())
print(para.__next__())
print(para.__next__())

# for name in names:
#     print(name)

# for char in para :
#     print(char)