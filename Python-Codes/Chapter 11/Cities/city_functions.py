def city_country(city, country, population=None):
    """
    Return a string formatted as 'City, Country' or
    'City, Country – population <population>' if provided.
    Example without population:
        city_country('santiago', 'chile') -> 'Santiago, Chile'
    Example with population:
        city_country('santiago', 'chile', 5000000)
        -> 'Santiago, Chile – population 5,000,000'
    """
    if population:
        return f"{city.title()}, {country.title()} – population {population:,}"
    else:
        return f"{city.title()}, {country.title()}"
