from localModules.car import Car,ElectricCar
#driver code
my_i8 = ElectricCar('BMW', 'I8', "2020")
print(my_i8.get_descriptive_name())
my_i8.battery.describe_battery()
my_i8.battery.get_range()
my_i8.battery.upgrade_battery()
my_i8.battery.get_range()
