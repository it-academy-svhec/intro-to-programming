module_name = "User Management"

menu = """
View all (1)
Find (2)
Add (3)
Update (4)
Delete (5)
Quit (q)
"""

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
                all(users)
            case '2':
                input('Enter search field')
                find(users, data)
            case _:
                print('Invalid option.')


def all(users):
    pass


def find(users, data):
    pass


def store(users, data):
    pass


def update(users, user, data):
    pass


def delete(users, user):
    pass
