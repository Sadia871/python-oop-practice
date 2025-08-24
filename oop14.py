class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, emp):
        self.department_name = department_name
        self.emp = emp

p = Employee("Talha")
d = Department("IT", p)

print(f"Employee Name: {p.name}")
print(f"Department Name: {d.department_name}")