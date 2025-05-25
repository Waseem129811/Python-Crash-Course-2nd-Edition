class Restaurant:
    """A simple representation of a restaurant with served count."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.lower()
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional):
        """Increment the number of customers served."""
        if additional >= 0:
            self.number_served += additional
        else:
            print("Cannot increment by a negative number.")


# Example usage
restaurant = Restaurant('pasta palace', 'italian')
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(20)
print(f"Customers served: {restaurant.number_served}")
