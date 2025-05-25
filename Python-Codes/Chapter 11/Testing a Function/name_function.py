def get_formatted_name(first_name, last_name):
    """
    Return a full name, neatly formatted.
    Example: get_formatted_name('janis', 'joplin') -> 'Janis Joplin'
    """
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name
