pizzas = ['margherita', 'pepperoni', 'hawaiian']
friend_pizzas = pizzas[:]   # Make a copy

pizzas.append('bbq chicken')
friend_pizzas.append('veggie')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
