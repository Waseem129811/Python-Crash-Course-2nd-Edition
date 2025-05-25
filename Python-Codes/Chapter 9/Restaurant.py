class Restaurant:
    """A simple representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.lower()

    def describe_restaurant(self):
        """Print the restaurant’s name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


# Example usage
restaurant = Restaurant('pasta palace', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
