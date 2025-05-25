class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}"


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range_miles = 240
        elif self.battery_size == 85:
            range_miles = 270
        print(f"This car can go approximately {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size < 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Example usage
electric_car = ElectricCar('tesla', 'model s', 2020)
electric_car.battery.describe_battery()  # Describe default battery (70 kWh)
electric_car.battery.get_range()         # Show range for 70-kWh battery

electric_car.battery.upgrade_battery()   # Upgrade to 85-kWh if not already
electric_car.battery.describe_battery()  # Describe new battery (85 kWh)
electric_car.battery.get_range()         # Show range for 85-kWh battery
