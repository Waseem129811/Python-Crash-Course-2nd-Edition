class Restaurant:
    """A simple representation of a restaurant with served count."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.lower()
        self.number_served = 0

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >= 0:
            self.number_served = number
        else:
            raise ValueError("Number served cannot be negative.")

    def increment_number_served(self, additional):
        """Increment the number of customers served."""
        if additional >= 0:
            self.number_served += additional
        else:
            raise ValueError("Increment must be non-negative.")
