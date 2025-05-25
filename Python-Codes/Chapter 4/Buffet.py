foods = ('steak', 'salad', 'soup', 'pasta', 'fish')
for food in foods:
    print(food)

# Attempting to change an element will raise an error:
# foods[0] = 'hamburger'  # TypeError: 'tuple' object does not support item assignment

# Redefine the tuple with new items:
foods = ('hamburger', 'salad', 'soup', 'pasta', 'ice cream')
for food in foods:
    print(food)
