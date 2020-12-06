import re 

text = "We 8 are 45 # @ ! $ + % good to go , 15 he  59 says 1"

founds = re.findall("[+]",text) # 00 - 58

print(founds)