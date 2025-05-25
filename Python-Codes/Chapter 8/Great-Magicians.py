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
