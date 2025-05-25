import random

class Die:
    """A simple model of a die."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll_die(self):
        """Return a random value between 1 and num_sides."""
        return random.randint(1, self.num_sides)
