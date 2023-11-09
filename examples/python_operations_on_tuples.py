user1 = (1, "johndoe@gmail.com", "John", "Doe")
user2 = (2, "linustorvalds@gmail.com", "Linus", "Torvalds")

# Length
print(f"There are {len(user1)} user fields.")

# Concatenate operator
user3_id_and_email = (3, "adalovelace@gmail.com")
user3_first_and_last_names = ("Ada", "Lovelace")

user3 = user3_id_and_email + user3_first_and_last_names

print(user3_id_and_email)
print(user3_first_and_last_names)
print(user3)

# Repeat operator
# Can be useful for setting defaults.
empty_user = ("", ) * 4

print(empty_user)

# Searching for elements
# Dynamically create list in for loop

found = False

for user in [user1, user2]:
    if "johndoe@gmail.com" in user:
        found = True
        break

print("Found user." if found else "User not found.")

print()

# Using not in instead
for user in [user1, user2]:
    if "johndoe@gmail.com" not in user:
        print("This is not John Doe.")
        break

    print("This is John Doe")
