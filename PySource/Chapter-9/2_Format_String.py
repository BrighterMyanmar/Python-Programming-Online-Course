name = input("Enter your name?\n")
age = input("Enter your age?\n")
heigh = input("Enter your heigh?\n")

answer = "Your name is {name} age is {age} and heigh is {heigh:.2f}"
answer = answer.format(age=age,heigh=float(heigh),name=name)
print(answer)

"""
    Indexed PlaceHolder
        answer = "Your name is {0} age is {2} heigh is {1}"
        answer = answer.format(name,heigh,age)
        print(answer)
    print(f'Name is {name} and age is {age} and heigh is {heigh}')
"""
