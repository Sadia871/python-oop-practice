def add_greeting_method(cls):
    def greet(self):
        return f"Hello from {self.__class__.__name__}!"
    cls.greet = greet
    return cls
@add_greeting_method
class Person:
    def __init__(self, name):
        self.name = name
p = Person("Sadia Saleem")
print(p.greet())
print(f"Employee Name: {p.name}")
# Output:
# Hello from Person!    
