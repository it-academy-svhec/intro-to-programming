def create_user_account(username, password="820BruceStreet"):
    print(f'Created user {username} with password "{password}"')


username = input("Enter a username: ")
password = input("Enter a password: ")

if not password:
    create_user_account(username)
else:
    create_user_account(username, password)
