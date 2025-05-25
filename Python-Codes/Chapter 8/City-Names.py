def city_country(city, country, population=None):
    """Return formatted city and country, optionally with population."""
    if population:
        return f"{city.title()}, {country.title()} — population {population:,}"
    return f"{city.title()}, {country.title()}"

# Example calls
print(city_country('santiago', 'chile', 5000000))
print(city_country('jakarta', 'indonesia'))
