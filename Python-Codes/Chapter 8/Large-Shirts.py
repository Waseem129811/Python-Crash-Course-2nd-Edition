def make_shirt(size='L', message="I love Python"):
    """Describe a T-shirt with default size and message."""
    print(f"Shirt size: {size}, Message: '{message}'.")

# Calls
make_shirt()                     # Large, default message
make_shirt(size='M')             # Medium, default message
make_shirt(message='Code Rocks') # Large, custom message
