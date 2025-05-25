import unittest
from restaurant import Restaurant

class RestaurantTestCase(unittest.TestCase):
    """Tests for Restaurant.number_served methods."""

    def setUp(self):
        """Create a Restaurant instance to test."""
        self.restaurant = Restaurant('Pasta Palace', 'Italian')

    def test_default_number_served(self):
        """The default number_served should be 0."""
        self.assertEqual(self.restaurant.number_served, 0)

    def test_set_number_served(self):
        """After setting number_served to 30, it should be 30."""
        self.restaurant.set_number_served(30)
        self.assertEqual(self.restaurant.number_served, 30)

    def test_increment_number_served(self):
        """After incrementing by 15, number_served should be 45."""
        self.restaurant.set_number_served(30)
        self.restaurant.increment_number_served(15)
        self.assertEqual(self.restaurant.number_served, 45)

    def test_set_number_negative_raises(self):
        """Setting a negative number should raise ValueError."""
        with self.assertRaises(ValueError):
            self.restaurant.set_number_served(-5)

    def test_increment_negative_raises(self):
        """Incrementing by a negative number should raise ValueError."""
        with self.assertRaises(ValueError):
            self.restaurant.increment_number_served(-10)

if __name__ == '__main__':
    unittest.main()
