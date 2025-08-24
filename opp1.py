# oop1.py

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Create objects
s1 = Student("Urwa", 21)
s2 = Student("Anaya", 22)

# Call method
print(s1.introduce())
print(s2.introduce())
print(s1.name)
print(s2.age)