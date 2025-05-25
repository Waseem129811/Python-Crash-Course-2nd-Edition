class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.cuisine_type.title()} cuisine.")

# Creating three restaurant instances
restaurant1 = Restaurant('burger barn', 'american')
restaurant2 = Restaurant('sushi spot', 'japanese')
restaurant3 = Restaurant('taco town', 'mexican')

# Calling describe_restaurant() on each
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
