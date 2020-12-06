fileName = "test.txt"
sarTar = """
    Lorem Ipsum is simply dummy text of the printing and 
    typesetting industry. Lorem Ipsum has been the industry's 
    standard dummy text ever since the 1500s, when an unknown 
    printer took a galley of type and scrambled it to make a type 
    specimen book. It has survived not only five centuries, but also 
    the leap into electronic typesetting, remaining essentially 
    unchanged. It was popularised in the 1960s with the release of 
    Letraset sheets containing Lorem Ipsum passages, and more recently 
    with desktop publishing software like Aldus PageMaker including 
    versions of Lorem Ipsum
""";

file = open(fileName,'r')
data = file.read()
file.close()
print(data)


"""
    t => text file
    b => binary file

    w => Write 
    r => read
    a => append
    x => create => file = open(fileName,'x')

    Write 
        file = open(fileName,'w')
        file.write(sarTar)
        file.close()
"""