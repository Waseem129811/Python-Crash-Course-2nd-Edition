def make_great(magicians):
    """Add 'the Great' to each magician's name and return a new list."""
    great_magicians = []
    for magician in magicians:
        great_magicians.append(magician + " the Great")
    return great_magicians

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

# Original list
magicians = ['alice', 'bob', 'carol']

# Make a copy of the list
original_magicians = magicians[:]

# Create the "great" list from the copy
great_magicians = make_great(original_magicians)

# Show both lists
print("Original magicians:")
show_magicians(original_magicians)

print("\nGreat magicians:")
show_magicians(great_magicians)
