class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The Car that was made at {self.year} {self.make} and it's model is {self.model} is starting.")


class  ElectricCar(Car):
    def start(self):
         print(f"The Elictric Car that was made at {self.year} {self.make} and it's model is {self.model} is starting.")

 
car = Car("Toyota", "Camry", 2022)

 
electricCar = ElectricCar("Tesla", "Model S", 2023)
 
car.start()            
electricCar.start()    