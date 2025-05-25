while True:
    artist = input("Enter artist (or 'quit' to stop): ")
    if artist.lower() == 'quit':
        break
    title = input("Enter album title (or 'quit' to stop): ")
    if title.lower() == 'quit':
        break
    album = make_album(artist, title)
    print(album)
