class fruit():
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size
    def intro(self):
        print(self.name)
        print(self.color)
        print(self.size)
apple=fruit("apple","red","small")
banana=fruit("bnana","yellow","big")
apple.intro()
banana.intro()
print(apple.name)
l1=["adam","zeeshan","sana","anakin","vilhelm"]
a1=enumerate(l1,start=15)
print(list(a1))