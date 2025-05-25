topping = ''
while True:
    topping = input("Enter a pizza topping (or 'quit'/'stop'): ")
    if topping.lower() in ['quit', 'stop']:
        break
    print(f"Adding {topping} to your pizza!")
print("Pizza complete.")
