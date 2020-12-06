import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

data = requests.get(base_url)

print(data.text)



"""
    custom Module => Written by us 
    build-in Module => Come with ptyhon 
    Third Party Module => pip install requests => Dependencies Manager
"""