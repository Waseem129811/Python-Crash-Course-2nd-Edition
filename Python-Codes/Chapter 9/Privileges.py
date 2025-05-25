class Privileges:
    """A class to store an admin’s privileges."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        """Print the list of privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class User:
    """A simple representation of a user."""

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


class Admin(User):
    """Represent an admin user with special privileges."""

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


# Example usage
admin_user = Admin('alice', 'smith', 30, 'new york')
admin_user.privileges.privileges = [
    'can add post', 'can delete post', 'can ban user'
]
admin_user.privileges.show_privileges()
