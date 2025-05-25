favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby'
}

people = ['jen', 'sarah', 'mike', 'alice']

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll!")
