def make_car(manufacturer, model, **options):
    """Return a dictionary of car information."""
    car = {'manufacturer': manufacturer.title(), 'model': model.title()}
    car.update(options)
    return car

# Example usage:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
