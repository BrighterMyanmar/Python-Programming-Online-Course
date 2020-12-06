import re

text = "We are 5 goood to go,3 Be he says @"

founds = re.findall("(go)",text) # d => find d character ; \d => digit number


print(founds)

""" 
    [] range or bunch of character
    \ special character escapse
    . any character
    ^ start with
    $ end with
    {} multiple specific character count
"""
