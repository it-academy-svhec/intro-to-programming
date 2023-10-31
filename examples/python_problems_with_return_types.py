def create_user_account(username, password):
    user = []

    if not username:
        return "No username provided."

    if len(password) < 8:
        return F"Password must be 8 characters. {len(password)} provided."

    user.append(username)
    user.append(password)

    return user


username = input("Enter a username: ")
password = input("Enter a password: ")

new_user = create_user_account(username, password)
print(f'Created user {new_user[0]} with password "{new_user[1]}"')
