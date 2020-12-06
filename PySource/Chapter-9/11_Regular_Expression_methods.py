import re

text = "We We are good to go, he We says"

result = re.split("e",text)
print(result)

"""
=> findall
    text = "Be are good to We go, he says"
    founds = re.findall('We',text)
    print(f"We found {len(founds)}") if len(founds) > 0 else print("No match Items")

=> search
    text = "We Be are good to  go, he says"
    founds = re.search("We",text)
    print(founds.group())
    print(founds.string)
    print(founds.span())

=> sub 
    result = re.sub("We","De",text)
    print(text)
    print(result)

=> split 
    result = re.split("e",text)
    print(result)
"""