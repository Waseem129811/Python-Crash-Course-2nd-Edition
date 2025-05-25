rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'danube': 'germany'
}

# Sentence about each river:
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print just the river names:
for river in rivers.keys():
    print(river.title())

# Print just the country names:
for country in rivers.values():
    print(country.title())
