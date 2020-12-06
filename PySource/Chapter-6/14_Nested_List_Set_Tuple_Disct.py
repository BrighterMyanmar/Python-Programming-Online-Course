data = [
    "One",
    "Two",
    ["Three","Four",("R","S","T"),{"U","V","W"},{"name":"Tun Tun","age":21},[1,2,3,4,5,6]],
    5,
    6.0,
    True,
    ("O","P","Q",["One","Two",["Q","B","C"]]),
    {"S","E","T",{'name':"Su Su"}},
    {'name':'Mg Mg','age':20,
        "family":{
            "father":"U Mya",
            "mother":"Daw Nu",
            "sibling":["Aung Aung","Tun Tun"]
        }
    }
]

for d in data:
    if(type(d) is list):
        for dd in d : 
            if(type(dd) is str) :
                print(f' String value {dd}')
            if(type(dd) is tuple):
                for tt in dd:
                    print(f'Tuple element {tt}')
            if(type(dd) is set):
                for ss in dd:
                    print(f'Set value {ss}')
            if(type(dd) is dict):
                for key,val in dd.items():
                    print(f'Key is {key} value is {val}')
            if(type(dd) is list) :
                for l in dd :
                    print(f'List value is {l}')
    if(type(d) is dict):
        for key in d.keys():
            print(f"Same Level {key}")
