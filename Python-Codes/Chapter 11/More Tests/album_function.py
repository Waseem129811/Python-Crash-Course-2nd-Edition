def make_album(artist, title, tracks=None):
    """
    Build a dictionary describing a music album.
    If 'tracks' is provided, include it in the dictionary.
    Example without tracks:
        make_album('pink floyd', 'the wall')
          -> {'artist': 'Pink Floyd', 'title': 'The Wall'}
    Example with tracks:
        make_album('metallica', 'ride the lightning', tracks=8)
          -> {'artist': 'Metallica', 'title': 'Ride The Lightning', 'tracks': 8}
    """
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks is not None:
        album['tracks'] = tracks
    return album
