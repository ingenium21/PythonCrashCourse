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