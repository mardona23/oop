class school:
    schoolname="adams school,school"
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def __display(self):
            print("Thos is a private method")
obg=school("adam","male",6985)
print(obg.schoolname)
obg.__display()