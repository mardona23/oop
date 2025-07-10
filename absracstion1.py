from abc import ABC, abstractmethod 
class abc(ABC):
    def intro(self,x):
        print(x)
    @abstractmethod
    def task(self):
        print(" i am in abstractmethod")
class test(abc):
    def task(self):
        return super().task()
obg1=test()
obg1.task()
obg1.intro(1239)