names = ["Mg Mg","Aung Aung","Tun Tun","Su Su"]
cities = ["Rangoon","Pago","Siggai","Hsipaw","Mandalay"]

for city in cities:
    print(city)
    if city == "Siggai":
        continue
    print("DDD")

i = 0;
while i < len(cities) :
    print(cities[i])
    if cities[i] == "Siggai" :
        i+=1
        continue
    i+=1 
    print("This is Extra")
    

print("Loop Done")
