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

my_rest = Restaurant("Renato's","Mexican")

my_rest.describe_restaurant()

my_rest.display_number_served()

my_rest.number_served = 23

my_rest.display_number_served()

my_rest.set_number_served(45)

my_rest.increment_number_served(10)

my_rest.display_number_served()
