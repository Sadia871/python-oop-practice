# class product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# @property
# def display_info(self):
#     return f"Product Name: {self.name}, Price: ${self.price}"
# @display_info.setter
# def display_info(self, info):
#     name, price = info.split(',')
#     self.name = name.strip()
#     self.price = float(price.strip().replace('$', ''))
# @display_info.deleter
# def display_info(self):
#     print(f"Deleting product: {self.name}")
#     del self.name
#     del self.price
# p = product("Laptop", 1200)
# print(p.display_info)
# p.display_info = "Smartphone, $800"
# print(p.display_info)
# del p.display_info
# # Output:
# # Product Name: Laptop, Price: $1200
# # Product Name: Smartphone, Price: $800
# #       
class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price}"

    @display_info.setter
    def display_info(self, info):
        name, price = info.split(',')
        self.name = name.strip()
        self.price = float(price.strip().replace('$', ''))

    @display_info.deleter
    def display_info(self):
        print(f"Deleting product: {self.name}")
        del self.name
        del self.price


# Test
p = product("Laptop", 1200)
print(p.display_info)   # Calls @property getter

p.display_info = "Smartphone, $800"  # Calls @setter
print(p.display_info)

del p.display_info   # Calls @deleter
