class vechile:
    def __init__(self,name,color,speed):
        self.name=name
        self.color=color
        self.speed=speed
    def intro(self):
        print(self.name)
        print(self.color)
        print(self.speed)
class bus(vechile):
    def __init__(self, name, color, speed, s):
        self.size=s
        vechile.__init__(self,name,color,speed)
a1=bus("lambogini","yellow","365","big")
print(a1.intro())