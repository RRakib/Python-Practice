class Student:
    def __init__(self,department,id,name):
        self.name = name
        self. id = id
        self.department = department
    def displayData(self):
        print(self.name,self.id,self.department)