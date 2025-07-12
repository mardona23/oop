class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y 
        return point(x,y)
    def __str__(self):
        return  f"({self.x}, {self.y})"
obg=point(46,58)
obj=point(83,94)
a=obg+obj
print(a)