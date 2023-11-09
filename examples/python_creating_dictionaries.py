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

user3 = {
    "id": 3,
    "email": "adalovelace@gmail.com",
    "first_name": "Ada",
    "last_name": "Lovelace"
}


users = [user1, user2, user3]

for user in users:
    print("ID:", user["id"])
    print("Email:", user["email"])
    print("First name:", user["first_name"])
    print("Last name:", user["last_name"])
    print()
