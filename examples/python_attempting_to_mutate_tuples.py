user1 = (1, "johndoe@gmail.com", "John", "Doe")
user2 = (2, "linustorvalds@gmail.com", "Linus", "Torvalds")
user3 = (3, "adalovelace@gmail.com", "Ada", "Lovelace")

users = [user1, user2, user3]

for user in users:
    for field in user:
        print(field)

print()

# Attempt to change email for John Doe
users[0][1] = "johndoe@yahoo.com"

#
