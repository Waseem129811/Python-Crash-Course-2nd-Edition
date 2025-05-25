def make_album(artist, title, tracks=None):
    """Return a dict representing a music album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album

# Example calls
print(make_album('pink floyd', 'the wall'))
print(make_album('metallica', 'ride the lightning', 8))
