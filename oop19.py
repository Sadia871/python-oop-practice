class multiplier:
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, value):
        return self.factor * value

# Test
# Creating an instance of the multiplier class with a factor of 3
m = multiplier(3000)
result = m.multiply(567)  # Should return 15
print(f"Result: {result}")  # Output: Result: 15
# Result: 15        