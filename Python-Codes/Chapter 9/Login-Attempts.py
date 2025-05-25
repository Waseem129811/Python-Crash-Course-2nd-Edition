class User:
    """A simple representation of a user with login attempts."""

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increment the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


# Example usage
user = User('alice', 'smith', 30, 'new york')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")  # Expected: 3

user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")  # Expected: 0
