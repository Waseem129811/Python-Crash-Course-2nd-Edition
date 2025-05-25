def make_sandwich(*ingredients):
    """Summarize the sandwich being ordered."""
    print("Making a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")

# Example calls:
make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'avocado')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')
