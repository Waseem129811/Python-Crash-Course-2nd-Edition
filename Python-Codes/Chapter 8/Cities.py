def city_country(city, country):
    """Return a string formatted 'City, Country'."""
    return f"{city.title()}, {country.title()}"

# Example calls
print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('paris', 'france'))
