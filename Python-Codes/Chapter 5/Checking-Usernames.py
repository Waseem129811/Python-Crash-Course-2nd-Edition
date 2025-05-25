current_users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
new_users = ['alice', 'david', 'Frank', 'Grace', 'BOB']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Username {user} is taken. Please enter a new username.")
    else:
        print(f"Username {user} is available.")
