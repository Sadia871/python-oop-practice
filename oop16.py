def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper
@log_function_call
def add(a, b):
    return a + b
result = add(3, 5)
# Output:
# Calling function: add
# Function add finished
print(f"Result: {result}")
# Output:
