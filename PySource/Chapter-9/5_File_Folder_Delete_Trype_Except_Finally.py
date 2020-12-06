import os


file_name = "test.txt"

try :
    if os.path.exists(file_name):
        os.remove(file_name)
    else :
        raise Exception("No such file","Fule Not found")  # Throw/raise new Exception 
except Exception as e:
    print(e.args[0])
finally :
    print("Everything is done!")

"""
    Delete File => os.remove(file_name)
    Delete Folder => os.rmdir("test")
"""