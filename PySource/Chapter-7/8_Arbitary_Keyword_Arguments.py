def show(**bm):
    for val in bm.values():
        print(val)
    for key,val in bm.items():
        print(f"Key is {key} and value is {val}")

def outPut(*bm):
    for x in bm:
        print(f'Value is {x}')


outPut("One","Two",3)
show(name="Mg Mg",age=20,heigh=5.11)