class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
    
    def drive(self):
        return f"the {self.brand} {self.model} is driving"
    
#object creation
my_car = Car('tesla', 'model S')

#call method
print(my_car.drive())
