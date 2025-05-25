import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_country()."""

    def test_city_country_without_population(self):
        """Return 'Santiago, Chile' when no population is given."""
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_with_population(self):
        """Return 'Santiago, Chile – population 5,000,000' when population is given."""
        result = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(result, 'Santiago, Chile – population 5,000,000')

if __name__ == '__main__':
    unittest.main()
