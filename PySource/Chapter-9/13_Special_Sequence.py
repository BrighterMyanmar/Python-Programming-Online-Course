import re 

text = "We are 4 # @ ! $ % good to go , 5 he says"

founds = re.findall("yasdf\Z",text)

print(founds)


"""
    Word Character => 
        -> a-z A-Z 0-9 _
    Special Character =>   
        -> !@#$%^&* " "
    Character => 
"""