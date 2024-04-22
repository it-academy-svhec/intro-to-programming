import users, module2

menu = f"""
User Management (1)
Module 2 (2)
Quit (q)
"""

option = ""

the_users = []

while option.lower() != "q":
    print()
    print("=" * 8 + "Main Menu" + "=" * 8)
    print(menu)
    
    option = input("Select an option: ")
    print()

    match option:
        case '1':
            users.run(the_users)
        case '2':
            module2.run()
        case _:
            print('Invalid option.')
