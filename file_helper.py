class FileHelper:

    def create(self,file_name):
        f = open(file_name,'x')
        f.close() 
        return True

    def read(self,file_name):
        f = open(file_name,'r')
        data = f.read() 
        return data

    def write(self,file_name,data):
        f = open(file_name,'w')
        f.write(data) 
        return True 

    def append(self,file_name,data): 
        f = open(file_name,'a') 
        f.write(data)
        f.close() 
        return True

    

    