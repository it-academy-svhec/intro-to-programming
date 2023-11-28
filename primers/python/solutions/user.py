def create(users, username, password):
    user = {
        "username": username,
        "password": password
    }

    if username and password:
        users.append(user)


def all(users):
    print("Users".center(40, "="))
    for user in users:
        print(user["username"], user["password"])
