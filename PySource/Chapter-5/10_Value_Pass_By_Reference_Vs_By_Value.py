ceetee = list(("Rangoon","Mandalay")) # memoty address #123 # ["Rangoon","Mandalay"]

bt = ceetee #bt =>  memoty address #123 # Value pass by Refrence

# ceetee[0] = "Hsipaw"
# bt[1] = "Siggai"

bt = ceetee.copy() # by value
bt[0] = "Hsipaw"

print(bt)
print(ceetee)