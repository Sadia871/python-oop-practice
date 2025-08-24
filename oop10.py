class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
dog = Dog("Jerman sharef", 3)
print(dog.bark())
print(f"Dog's Name: {dog.name}, Age: {dog.age}")
# # OOPs Assignment 10
# ### 10. **Classes and Objects**