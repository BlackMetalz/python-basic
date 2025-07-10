# Defination of Car class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.year} {self.make} {self.model} is starting."

    def stop(self):
        return f"{self.year} {self.make} {self.model} is stopping."

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
def main():
    print("__name__: %s" % __name__)
    toyota_car = Car("Toyota", "Corolla", 2020)
    print(toyota_car.start())  # Output: 2020 Toyota Corolla is starting.
    print(toyota_car.stop())   # Output: 2020 Toyota Corolla is stopping.
    print(toyota_car)          # Output: 2020 Toyota Corolla

    honda_car = Car("Honda", "Civic", 2019)
    print(honda_car.start())  # Output: 2019 Honda Civic is starting.
    print(honda_car.stop())   # Output: 2019 Honda Civic is stopping.
    print(honda_car)          # Output: 2019 Honda Civic

if __name__ == "__main__":
    main()