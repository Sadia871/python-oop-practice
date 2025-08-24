class Engine:
    def start(self):
        print("Engine started")
    def stop(self):
        print("Engine stopped")
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        self.engine.stop()
        print(f"{self.make} {self.model} is stopping.")
car = Car("Toyota", "Corolla")
car.start()
car.stop()
# # OOPs Assignment 13