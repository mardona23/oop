class vehicle:
    def __init__(self,number_of_seats,name):
        self.name=name
        self.number_of_seats=number_of_seats
    def intro(self):
        print(self.name)
        print(self.number_of_seats)
class bus(vehicle):
    def __init__(self, number_of_seats, name):