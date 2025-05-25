def get_formatted_name(first_name, last_name, middle_name=''):
    """
    Return a full name, neatly formatted.
    If a middle_name is provided, include it.
    Example without middle name: get_formatted_name('janis', 'joplin')
        -> 'Janis Joplin'
    Example with middle name: get_formatted_name('john', 'hooker', 'lee')
        -> 'John Lee Hooker'
    """
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name
