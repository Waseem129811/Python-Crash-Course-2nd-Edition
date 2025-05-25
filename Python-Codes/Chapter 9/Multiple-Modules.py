class Car:
    """A simple representation of a car."""

    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range_miles = 240
        elif self.battery_size == 85:
            range_miles = 270
        else:
            range_miles = "an unknown number of"

        print(f"This car can go approximately {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Create an electric car and demonstrate battery features
my_tesla = ElectricCar('tesla', 'model s', 2024)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrade the battery and show the new range
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
