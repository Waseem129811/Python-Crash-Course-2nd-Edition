class User:
    """A simple representation of a user."""

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()

    def describe_user(self):
        """Print user information."""
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")


# Example usage
user1 = User('alice', 'smith', 30, 'new york')
user2 = User('bob', 'johnson', 45, 'chicago')

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
