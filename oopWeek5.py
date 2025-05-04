# Assignment 1: Car Class
class Car:
    def __init__(self, brand, model, color):
        """
        Initialize a car with brand, model, and color.
        
        Args:
            brand (str): The car's brand.
            model (str): The car's model.
            color (str): The car's color.
        """
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        """Print a message indicating the car is driving."""
        print(f"The {self.color} {self.brand} {self.model} is driving smoothly!")

# Create and test a Car instance
my_car = Car(brand="Toyota", model="Corolla", color="Blue")
print(my_car.brand)
my_car.drive()
print(my_car.model)
print(my_car.color)
