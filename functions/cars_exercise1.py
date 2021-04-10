class Car:
    """This class describe model of the car."""
    def __init__(self, model, color, brand):
        """this is constructor, with required parameters."""
        self.model_of_the_car = model
        # a global variable (self.brand)
        self.color_of_the_car = color
        self.brand_of_the_car = brand

    def drive(self):
        """driving action"""
        if self.brand_of_the_car.lower() == 'bmw':
            print(f"You are driving Fast! isn't it awesome?")

        else:
            print(f"You are driving the car! isn't it awesome?")

    def do_something(self):
        print("I want to do something...")
        print("let me drive this car;)")
        self.drive()

    def get_description(self):
        """ """
        # print(f" Brand of hte car{self.brand) we are using here local variable thet is only inside init method
        print(f"Model of hte car: {self.model_of_the_car}")
        print(f"Color of hte car: {self.color_of_the_car}")
        print(f"Brand of hte car: {self.brand_of_the_car}")
class ElectricCar(Car):
    """This is the child class of Car. ElectricCar class inherits from Car class"""
    def __init__(self, brand, model, color):
        """This is the constructor, with required parametrs"""
        super().__init__(brand, model, color)
        self.battery_size = 60
    def get_battery_info(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_description(self):
        super().get_description()
        print(f"Battery size of car: {self.battery_size}")
