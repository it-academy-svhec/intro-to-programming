import user


def test_can_create_user():
    # Arrange
    users = []

    username = "johndoe"
    password = "password123"

    # Act
    user.create(users, username, password)

    # Assert
    the_user = {
        "username": username,
        "password": password
    }

    assert the_user in users


def test_cannot_create_user_without_required_fields():
    users = []

    user.create(users, "", "")

    the_user = {
        "username": "",
        "password": ""
    }

    assert the_user not in users
