class vehicle:
    def __init__(self,number_of_seats,name):
        self.name=name
        self.number_of_seats=number_of_seats
    def intro(self):
        print(self.name)
        print(self.number_of_seats)
class bus(vehicle):
    def __init__(self, number_of_seats, name,distance ):
        self.distance=distance
    def __init__(self,number_of_seats,name):     
    def fare(self,distance):
        print(distance*126)
    vehicle.. __init__(self,number_of_seats,name)
obg1=bus(23,"mercedes")
obg1.intro()
obg1.fare(2)