def get_valid_age():
    while True:
        user_input = input("Enter your age: ")
        if user_input.isdigit() and 0 <= int(user_input) <= 120:
            return int(user_input)
        else:
            print("Invalid age. Please enter a valid age between 0 and 120.")


age = get_valid_age()
print("Your age is:", age)
