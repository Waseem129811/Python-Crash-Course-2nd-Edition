def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {'first_name': first.title(), 'last_name': last.title()}
    profile.update(user_info)
    return profile

# Example usage
user_profile = build_profile(
    'albert', 'einstein',
    location='princeton',
    field='physics',
    occupation='theoretical physicist'
)
print(user_profile)
