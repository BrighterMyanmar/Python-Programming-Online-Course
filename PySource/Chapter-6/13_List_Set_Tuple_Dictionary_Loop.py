nameList = ["Mg Mg","Aung Aung","Tun Tun","Su Su"]
nameTupel = ("Mg Mg","Aung Aung","Tun Tun","Su Su")
nameSet = {"Mg Mg","Aung Aung","Tun Tun","Su Su"}
nameDictionary = {
    "name":"Mg Mg",
    "age":20,
    "heigh":5.9,
    "city":"Rangoon"
}

for ind,name in enumerate(nameTupel,start=1):
    print(f'Name is {name} and its index is {ind}')

for x in range(1,len(nameList)-1):
    print(nameList[x])
print("****************  **********************")
for x in range(0,len(nameTupel),2):
    print(nameTupel[x])

print("**************** Dictionary Loop **********************")
for key,val in nameDictionary.items():
    print(f"Key is {key} and value is {val}")

for key in nameDictionary.keys():
    print(key)

for key in nameDictionary:
    print(f'Key is {key} value is {nameDictionary[key]}')

for val in nameDictionary.values() :
    print(val)

print("**************** Set Loop **********************")
for name in nameSet:
    print(name)
print("**************** Tuple Loop **********************")
for name in nameTupel:
    print(name)

print("**************** List Loop **********************")
for name in nameList:
    print(name)
