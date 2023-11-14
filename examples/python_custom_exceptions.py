class InvalidUsernameError(Exception):
    def __init__(self, message="Username must be at least 6 characters."):
        self.message = message
        super().__init__(self.message)


class InvalidPasswordError(Exception):
    def __init__(self, message="Password must be at least 8 characters."):
        self.message = message
        super().__init__(self.message)


def create_user_account(username, password):
    try:
        if len(username) <= 6:
            raise InvalidUsernameError()

        if len(password) <= 8:
            raise InvalidPasswordError()

        print(f'Created user {username} with password "{password}"')
    except InvalidUsernameError as e:
        print(e.message)
    except InvalidPasswordError as e:
        print(e.message)


username = input("Enter a username: ")
password = input("Enter a password: ")

create_user_account(username, password)
