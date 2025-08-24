class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    def to_kelvin(self):
        return self.celsius + 273.15
converter = TemperatureConverter(25)
print(f"{converter.celsius}°C is {converter.to_fahrenheit()}°F")
print(f"{converter.celsius}°C is {converter.to_kelvin()}K")
# # OOPs Assignment 12