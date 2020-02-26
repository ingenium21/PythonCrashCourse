class Car:
    #A simple attempt to represent a car

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back the odometer!")
    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't add negative miles")

class Battery:
    # A simple attempt to model a battery for an electric car

    def __init__(self, battery_size = 75):
        #Initialize the battery's attributes
        self.battery_size = battery_size
    
    def describe_battery(self):
        #print a statement describing the battery size
        print(f"This car has a {self.battery_size}kWh battery.")
    
    def get_range(self):
        #print the range the type of battery provides
        if self.battery_size == 75:
            range = 260
        
        elif self.battery_size == 100:
            range = 315
        
        print(f"this car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"this battery has been upgraded to a {self.battery_size}kWh battery")
    

class ElectricCar(Car):
    #Represents aspects of a car specific to electric vehicles

    def __init__(self, make, model, year):
        #initialize attributes of the parent class
        super().__init__(make, model, year)
        self.battery = Battery()

#driver code
my_i8 = ElectricCar('BMW', 'I8', "2020")
print(my_i8.get_descriptive_name())
my_i8.battery.describe_battery()
my_i8.battery.get_range()
my_i8.battery.upgrade_battery()
my_i8.battery.get_range()
