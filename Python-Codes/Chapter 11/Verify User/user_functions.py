def verify_user(username, active_users):
    """
    Return True if 'username' (case-insensitive) is in 'active_users'; otherwise False.
    Example: verify_user('Alice', ['alice', 'bob']) -> True
    """
    username_lower = username.lower()
    active_lower = [user.lower() for user in active_users]
    return username_lower in active_lower
