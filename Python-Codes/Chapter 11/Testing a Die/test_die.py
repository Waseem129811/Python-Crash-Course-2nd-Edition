import unittest
from die import Die

class DieTestCase(unittest.TestCase):
    """Tests for the Die class."""

    def test_roll_die_within_range(self):
        """A single roll should be between 1 and num_sides."""
        die = Die()  # Default 6-sided
        roll = die.roll_die()
        self.assertIn(roll, range(1, die.num_sides + 1),
                      "roll_die() returned a value outside 1–6")

    def test_roll_die_all_values(self):
        """Rolling the die 100 times should produce all possible faces."""
        die = Die()
        results = [die.roll_die() for _ in range(100)]
        for side in range(1, die.num_sides + 1):
            self.assertIn(side, results,
                          f"Value {side} did not appear in 100 rolls")

    def test_custom_sided_die(self):
        """A die with a non-default number of sides still rolls properly."""
        die = Die(num_sides=10)
        roll = die.roll_die()
        self.assertIn(roll, range(1, 11),
                      "roll_die() returned a value outside 1–10 for a 10-sided die")

if __name__ == '__main__':
    unittest.main()
