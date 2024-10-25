#7.Write a Python program to demonstrate class, object and accessing class members example.

class Car: 
 def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
 def display(self):
    print(f'car make:{self.make}')
    print(f'car model:{self.model}')
    print(f'car year:{self.year}')
mycar = Car('toyota','corolla',2020)
print(f'makes:{mycar.make}')
print(f'model:{mycar.model}')
print(f'year:{mycar.year}')

      
