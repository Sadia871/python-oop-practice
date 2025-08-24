# # OOPs Assignment 7      
#     ### 7. **Access Modifiers: Public, Private, and Protected** 
# #Create a class `Employee` with:
# # - a public variable `name`,
# # - a protected variable `_salary`, and
# # - a private variable `__ssn`.  
# #Try accessing all three variables from an object of the class and document what happens.

class Employee :
  def __init__(self , name : str , salary : int , atm_pin):
    self.name = name
    self._salary = salary
    self.__atm_pin = atm_pin
emp = Employee("Sadia" , 80000 , 7890)
print(emp.name)
print(emp._salary)
print(emp._Employee__atm_pin)