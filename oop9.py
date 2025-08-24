from abc import ABC, abstractmethod 
class Employee(ABC):
    def __init__(self, name: str, salary: int, atm_pin: int):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__atm_pin = atm_pin  # Private variable

    @abstractmethod
    def display_info(self):
        pass
class FullTimeEmployee(Employee):
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}, ATM PIN: {self._Employee__atm_pin}")
emp = FullTimeEmployee("Sadia", 80000, 7890)
emp.display_info()