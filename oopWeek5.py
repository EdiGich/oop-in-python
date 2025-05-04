# Assignment 1: Car Class
class Car:
    def __init__(self, brand, model, color):
        """
        Initialize a car with brand, model and color.
        
        Args:
            brand (str): The car's brand.
            model (str): The car's model.
            color (str): The car's color.
        """
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        """Print a message showing that the car is driving."""
        print(f"The {self.color} {self.brand} {self.model} is driving smoothly!")

# Create and test a Car instance
my_car = Car(brand="Toyota", model="Corolla", color="Blue")
print(my_car.brand)
my_car.drive()
print(my_car.model)
print(my_car.color)


# Activity 2. Car Type Polymorphism
class Vehicle:
    def move(self):
        """Base move method to be overridden."""
        pass

class SportsCar(Vehicle):
    def move(self):
        """Polymorphic move method for sports cars."""
        print("moves fast")

class Truck(Vehicle):
    def move(self):
        """Polymorphic move method for trucks."""
        print("Heavy load!")

# Create and test Vehicle instances
sports_car = SportsCar()
truck = Truck()

sports_car.move()
truck.move()

# Demonstrate polymorphism with a list
vehicles = [sports_car, truck]
for vehicle in vehicles:
    vehicle.move()
