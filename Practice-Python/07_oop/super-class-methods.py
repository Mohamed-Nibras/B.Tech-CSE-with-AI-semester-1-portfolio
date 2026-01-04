class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def movement(self):
        print('Vehicle is moving ')

class Car(Vehicle):
    def __init__(self, make, model, license_id):
        super().__init__(make, model)
        self.license_id = license_id

    def movement(self):
        super().movement()
        print(f"{self.make} is moving on the road ")
    


car1 = Car("Tata", "Safari", "2007")
print(car1.model)
car1.movement()

