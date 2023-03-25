
class Restaurant:
    def _init_(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant name: {self.name} ")
        print(f"Cuisine type:  {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant opens from 6pm-12pm")

restaurant_1 = Restaurant('Delhi76','Indian food')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant() 