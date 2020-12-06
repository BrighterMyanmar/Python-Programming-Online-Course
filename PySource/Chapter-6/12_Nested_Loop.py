names = [
    ["Mg Mg","Aung Aung","Tun Tun","Su Su"],
    ["One","Two","Three"],
    ["Toyota","Alphbert","LandCruiser","Swift"]
]

p = 0

while p < len(names) :
    parent = names[p]
    t = 0 
    while t < len(parent) :
        print(parent[t])
        t+=1
    print("****************** One List Done *******************")
    p+=1

for parent in names:
    print(parent)
    for children in parent:  
        print(children)

    print("****************** One List Done *******************")

