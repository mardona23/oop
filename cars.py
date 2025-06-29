class car():
    def __init__(self,name,color,size,model):
        self.name=name
        self.color=color
        self.size=size
        self.model=model
    def intro():
        print(self.name)
        print(self.color)
        print(self.size)
        print(self.model)
mclaren=car("mclaren","black","small","mclaren720")
tesla=car("tesla","red","small","teslax")
audi=car("audi","blue","big","audiq4")
bmw=car("bmw","green","big","bmwx")
mclaren.intro()
tesla.intro()
audi.intro()
bmw.intro()
print(mclaren.name)
l1=["adam","ejgil","anakin","boiwe","oliver"]
g1=enumerate(l1,start=15)
print(list(g1))