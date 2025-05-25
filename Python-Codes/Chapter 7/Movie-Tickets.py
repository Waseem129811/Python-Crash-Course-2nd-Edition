prompt = "Enter your age (or 'quit' to exit): "
while True:
    age_input = input(prompt)
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket cost is ${price}.")
