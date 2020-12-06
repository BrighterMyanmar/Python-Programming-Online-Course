import requests 
import json

base_url = "https://jsonplaceholder.typicode.com/posts"
user_api_url = "https://randomuser.me/api/?results=50"

users_str = requests.get(user_api_url)
print(users_str.text)

# x = requests.get(base_url).text
# postList = json.loads(x) # [ {},{},{}]

# print(len(postList))
# lastIndex = len(postList)-1;
# print(postList[lastIndex]["userId"])
# print(postList[lastIndex]["id"])
# print(postList[lastIndex]["title"])
# print(postList[lastIndex]["body"])