import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for get_formatted_name()."""

    def test_first_last_name(self):
        """Do names like 'janis joplin' work?"""
        formatted = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
