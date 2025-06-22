class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def intro(self):
        print(self.name)
        print(self.grade)
ob1=student("vilhelm",2)      
ob1.intro()