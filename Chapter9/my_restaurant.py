from localModules.restaurant import Restaurant,IceCreamStand

#driver code
my_rest = Restaurant("Renato's","Mexican")

my_rest.describe_restaurant()

my_rest.display_number_served()

my_rest.number_served = 23

my_rest.display_number_served()

my_rest.set_number_served(45)

my_rest.increment_number_served(10)

my_rest.display_number_served()

my_iceCreamStand = IceCreamStand("Rennies", "Dessert")
my_iceCreamStand.describe_restaurant()

my_iceCreamStand.open_restaurant()

my_iceCreamStand.list_flavors()
