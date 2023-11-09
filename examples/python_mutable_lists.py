# Starts as empty list
users = []

# Mutates to list with one element.
# Nested list of lists. Each sublist represents a user.
users.append([1, "johndoe@gmail.com", 25, 524.32, False])


def print_user(user):
    display_status = "Enabled" if user[4] else "Disabled"

    print("======User Information======")
    print(
        f"ID: {user[0]}\nEmail: {user[1]}\nAge: {user[2]}\nBalance: \
            {user[3]}\nAccount Status: {display_status}\n")


print_user(users[0])

# Accidentially mutate user ID
users[0][0] = 7

# Intentionally mutate data
users[0][1] = "johndoe@outlook.com"
users[0][2] = 26
users[0][3] = 200
users[0][4] = True

print_user(users[0])

# Mutate list by deleting the user
del users[0]

try:
    print_user(users[0])
except IndexError:
    print("User not found.")
