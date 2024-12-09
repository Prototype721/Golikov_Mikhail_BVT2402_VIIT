class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return (self.make, self.model)
    

class Car(Vehicle):
    def __init__(self, make, model, fuel):
        super().__init__(make, model)
        self.fuel = fuel

    def get_info(self):
        return (self.make, self.model, self.fuel)
    
Veh_1 = Vehicle(make='Boeing', model='737-Max')
Veh_2 = Car(make='Bugatti', model='Chiron', fuel='Nucklear')

print(Veh_1.get_info())
print(Veh_2.get_info())
