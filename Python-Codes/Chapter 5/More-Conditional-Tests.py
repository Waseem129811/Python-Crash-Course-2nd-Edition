name = "Alice"
print("Is name.lower() == 'alice'? I predict True.")
print(name.lower() == "alice")   # True

print("Is name == 'alice'? I predict False.")
print(name == "alice")           # False

age = 20
print("Is age > 18? I predict True.")
print(age > 18)                  # True

print("Is age < 18? I predict False.")
print(age < 18)                  # False

print("Is 15 <= age < 25? I predict True.")
print(15 <= age < 25)            # True

print("Is age == 21 or age == 20? I predict True.")
print(age == 21 or age == 20)    # True

print("Is age != 20? I predict False.")
print(age != 20)                 # False

fruits = ['apple', 'banana', 'cherry']
print("'banana' in fruits? I predict True.")
print('banana' in fruits)        # True

print("'orange' not in fruits? I predict True.")
print('orange' not in fruits)    # True

numbers = [1, 2, 3, 4, 5]
print("Is 3 in numbers? I predict True.")
print(3 in numbers)              # True

print("Is 10 in numbers? I predict False.")
print(10 in numbers)             # False
