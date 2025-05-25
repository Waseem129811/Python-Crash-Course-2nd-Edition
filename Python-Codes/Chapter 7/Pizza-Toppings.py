topping = ''
while topping.lower() != 'quit':
    topping = input("Enter a pizza topping (type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza!")
print("Finished making your pizza.")
