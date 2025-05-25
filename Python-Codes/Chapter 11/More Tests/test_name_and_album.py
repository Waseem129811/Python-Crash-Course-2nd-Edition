import unittest
from name_function import get_formatted_name
from album_function import make_album

class NamesTestCase(unittest.TestCase):
    """Tests for get_formatted_name()."""

    def test_first_last_name(self):
        """Do names like 'janis joplin' work?"""
        formatted = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Do names like 'john lee hooker' work?"""
        formatted = get_formatted_name('john', 'hooker', 'lee')
        self.assertEqual(formatted, 'John Lee Hooker')

class AlbumTestCase(unittest.TestCase):
    """Tests for make_album()."""

    def test_make_album_without_tracks(self):
        """Can we make an album dict without tracks?"""
        album = make_album('pink floyd', 'the wall')
        expected = {'artist': 'Pink Floyd', 'title': 'The Wall'}
        self.assertEqual(album, expected)

    def test_make_album_with_tracks(self):
        """Can we make an album dict with a track count?"""
        album = make_album('metallica', 'ride the lightning', tracks=8)
        expected = {
            'artist': 'Metallica',
            'title': 'Ride The Lightning',
            'tracks': 8
        }
        self.assertEqual(album, expected)

if __name__ == '__main__':
    unittest.main()
