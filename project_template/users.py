module_name = "User Management"

menu = """
View all (1)
Find (2)
Add (3)
Update (4)
Delete (5)
Quit (q)
"""

# User dictionary keys: id, first_name, last_name

def run(users):
    print("=" * 8 + module_name + " Menu" + "=" * 8)
    print(menu)
    
    option = ""
    
    while option.lower() != "q":
        print()
        print("=" * 8 + module_name + " Menu" + "=" * 8)
        print(menu)
        
        option = input("Select an option: ")
        print()

        match option:
            case '1':
                print(all(users))
            case '2':
                search_term = input('Enter search term')
                
                user = find(users, search_term)
                
                display(user)
            case '3':
                user_fields = {
                    'first_name': input('Enter first name:'),
                    'last_name': input('Enter last name:'),
                }
                
                user = store(users, user_fields)
            case '4':
                user = update(users, user, user_fields):
            case _:
                print('Invalid option.')


def all(users):
    formatted_users = "=" * 8 + 'Users' + "=" * 8 + '\n'
    
    for user in users:
        formatted_users += user['first_name'] + ' ' + user['last_name'] + '\n'
        
    return formatted_users or "No users"


def find(users, search_term):
    for user in users:
        for field in user.values():
            if field == search_term:
                return user
    else:
        return "User not found"


def store(users, user_fields):
    users.append(user_fields)


def update(users, id, new_data):
    for user in users:
        if id == user.id:
            index = users.index(user)
            users[index] = new_data


def delete(users, user):
    pass


def display(user):
    print("=" * 8 + 'User Info' + "=" * 8)
    print(user['first_name'], user['last_name'])
