class Restaurant: 
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"My Restaurant's name is {self.name}")
        print(f"And we serve {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is now open")

    def close_restaurant(self):
        print(f"{self.name} is now closed")
    
    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self,increment):
        self.number_served += increment
    
    def display_number_served(self):
        #display how many served
        print(f"Where {self.number_served} have been served")

class IceCreamStand(Restaurant):
    # child class for specific type of Restaurant
    def __init__(self, name, cuisine):
        #initialize attributes of parent class
        super().__init__(name, cuisine)
        self.flavors = ['strawberry', 'chocoate', 'vanilla']

    def list_flavors(self):
        print("our Ice Cream flavors are: ")
        for i in self.flavors:
            print(i)

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
