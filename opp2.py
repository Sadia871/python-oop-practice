### 2. **Using `cls`**
#Create a class `Counter` that keeps track of how many objects have been created. Use a class variable and a class method with `cls` to manage and display the count.

class Counter:
  count = 0
  def __init__(self):
    Counter.count += 1
  @classmethod
  def display(cls):
    print("Object have been created like :" , cls.count)
A1 = Counter()
A2 = Counter()
A3 = Counter()
A4 = Counter()
A5 = Counter()
A6 = Counter()
A1.display()