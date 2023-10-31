# Initialize users with None
users = None

name = input("Enter a user's name: ")

if name:
    users = [name]

if users == None:
    print('No users have been created')
else:
    for user in users:
        print(user)
