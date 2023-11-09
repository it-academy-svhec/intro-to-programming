user1 = {
    "id": 1,
    "email": "johndoe@gmail.com",
    "first_name": "John",
    "last_name": "Doe"
}

user2 = {
    "id": 2,
    "email": "linustorvalds@gmail.com",
    "first_name": "Linus",
    "last_name": "Torvalds"
}

users = [user1, user2]

print(users)

for user in users:
    del user["first_name"]
    del user["last_name"]

print(users)
