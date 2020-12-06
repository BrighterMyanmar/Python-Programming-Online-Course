x = 20 # Global Scope

def aa():
    global y;
    y = 30 # global Scope
    print(f'From aa {y}')
    def bb():
        z = 40 # local Scope
        print(f'From bb {x}')
        def cc():
            print(f'From cc {x}')
        cc()
    bb()

aa()

print(f'Y is {y}')



"""
    Global Scope
    local Scope
    Lexical Scope
    global keyword
"""