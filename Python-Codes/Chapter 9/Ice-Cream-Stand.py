class Restaurant:
    """A simple representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.lower()

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):
    """Represent an ice cream stand, a specific kind of restaurant."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Print the list of available flavors."""
        print(f"Flavors available at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# Example usage
ice_cream_stand = IceCreamStand('frosty treats')
ice_cream_stand.flavors = ['vanilla', 'chocolate', 'strawberry']
ice_cream_stand.display_flavors()
