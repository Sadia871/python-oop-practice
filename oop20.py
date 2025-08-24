class invalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Invalid age: {self.age}. Age must be between 0 and 120."
class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0 or age > 120:
            raise invalidAgeError(age)
        self.age = age
# Test
try:
    p1 = Person("Alice", 30)
    print(f"Person created: {p1.name}, Age: {p1.age}")

    p2 = Person("Bob", -5)  # This will raise an exception
    print(f"Person created: {p2.name}, Age: {p2.age}")
except invalidAgeError as e:
    print(e)
# Output: