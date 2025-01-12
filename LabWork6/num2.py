class Vichle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def get_info(self):
        return f'Марка:{self.make}, модель:{self.model}'
class Car(Vichle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type = fuel_type
    def get_info(self):
        return f'Марка:{self.make}, модель:{self.model}, тип топлива:{self.fuel_type}'
car = Car('a','b','c')
print(car.get_info())