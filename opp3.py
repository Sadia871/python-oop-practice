class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
# Create objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)
car4 = Car("Chevrolet", "Malibu", 2018)
car5 = Car("Nissan", "Altima", 2022)
# Call method
print(car1.display_info())
print(car2.display_info())
print(car3.display_info())
print(car4.display_info())
print(car5.display_info())


### 3. **Using `self` and `cls`**
#Create a class `Bank