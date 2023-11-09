def create_user_account(username, password="820BruceStreet"):
    print(f'Created user {username} with password "{password}"')
    return [username, password]


username = input("Enter a username: ")

new_user = create_user_account(username)
print(new_user[0], new_user[1])

username = input("Enter a username: ")

create_user_account(username)
