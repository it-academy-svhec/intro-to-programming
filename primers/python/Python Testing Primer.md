# Testing Primer

## Conceptual Overview

Testing is a fundamental aspect of the software development process.
This can be done manually or automatically. As developers, we often prefer automated testing because this is faster and more efficient.
Not all aspects of a program can be automatically test, but most can. Test suites are created that contain individual tests to assert that the code behaves as expected.

There are two primary types of tests: unit tests and integration tests. Unit tests check the behavior of small and cohesive building blocks in your code.
For instance, you could write a unit test to ensure that a function returns a specific results given specific inputs. Integration tests check the behavior of more complex subsystems in the application, such as a user authentication module. For example, we could write a test to make sure that a user can log in and then is presented with welcome text. Then we could check that they can perform certain actions. This test will involve code from many different units in the system.

Good test plans should include both unit and integration tests.

## Task Overview

Let's create a basic module with some functions to manage user accounts. Then we will create a main Python script to run the functions. Next we will create some tests to ensure our code works as expected.

## Setting Up Modules

In order to write unit tests, we need to organize our code into modules, which are separate Python script files. A set of related, cohesive functions will be defined inside a module file. Then we can import the code from the module file into other scripts and call the module functions.

1. Create a folder where you store source code on your local machine named `Python Testing Primer`

1. Open the folder in VS Code

1. Create a file named `user.py` which will represent a module containing functions for managing user accounts

1. Add the following function to create a new user

   ```python
   def create(users, username, password):
       user = {
           "username": username,
           "password": password
       }

   users.append(user)
   ```

1. Add the following function to view all users

   ```python
   def all(users):
        print("Users".center(40, "="))
        for user in users:
            print(user["username"], user["password"])
   ```

1. Create a file named `main.py`. This is a runner file that will use the functions defined in the `user.py` module.

1. Add the line below to `main.py`. This will import the `user.py` module into `main.py`.

   ```python
   import user.py
   ```

1. Define an empty list called `users`

1. Then call the `create` function inside the `user` module by entering the following. Note that the dot operator (`.`) is used to indicate that we want the `create` function inside the `user.py` file.

   ```python
   user.create(users, "johndoe", "password")
   ```

1. Use a similar method to call the `all` function on the `users` list

1. Run the program and should see the contents of the `users` list

## Testing Strategy

In general, we want to the follow this process during each test:

1. Arrange: set up test data
2. Act: run functions we are testing
3. Assert: check the output against expectations

## Creating Simple Unit Tests

Let's create a suite of unit tests to make sure our `user.py` module behaves properly given a range of inputs. It's not enough to simply manually test with one set of inputs. If we want good quality software, we need to use a robust and wide range of inputs and check the outputs.

There are many different tools for creating and running automated tests in Python. Python provides a first-party module called `unittest` that is commonly used. We will use `pytest` though since it does not require us to use Python classes (OOP) concepts to write tests.

1. Create a file named `test_user.py`

1. The testing tool `Pytest` must be installed using the `pip` CLI package manager for Python. Run the following command to install the latest version of `Pytest`. You can use `pip` to install packages that other Python developers have created to enhance your programs.

   ```
   pip install pytest
   ```

1. Open the `test_user.py` file

1. Enter the following code to create a function that will run in the test called `test_can_create_user`.

   ```python
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
   ```

   **Line-by-line explanation**

   First we import the `user` module into the test file. Then we define a test function called `test_can_create_user`. This function is called every time we run our test suite. On the arrange step, we define an empty list called `users` and then choose a username and password for the test user. Next, we act by calling the `create` function in the `user` module. Finally, we assert by using the `assert` keyword to see if the `the_user` dictionary is in the `users` list. The `assert` keyword raises and exception if the expression to the right (`the_user in users`) evaluates to `False`. Otherwise, it is `True` and the test passes.

1. Run the `pytest -rA` command in the VS Code integrated Terminal to run launch the tests. The parameters instruct Pytest to show the result of each test. The test should pass.

1. Now create a test to make sure that a user without a username or password cannot be created. Call the function `test_cannot_create_user_without_required_fields`.

1. Run the tests again. The first test should pass, but the second should fail. Testing is all about finding bugs. In this case, the bug is that users can be created without a username or password.

1. Refactor the `create` function in the `user` module to make this test pass, which would indicate that the bug is most likely fixed

## Writing More Tests

Try writing tests for ensure that the `all` function works as expected.

- It is difficult to test functions when they produce console output via `print` statements. You will need to refactor the function to return the text that should be printed as a string rather than actually printing the text.
- You will need to make some changes to the `main.py` file as well since the function will not print the output.
- Arrange: create a `users` list and then add a user to it.
- Act: get the string of all users in the `users` list
- Assert: check if the user you added is in the string output returned by the `all` function

## Optional - Configure VS Code for Python Testing

1. Click the Testing option on the left nav bar in VS Code

1. Click Configure Python Tests

1. Select the test framework. In this primer, we used the Pytest framework

1. Select the directory that contains the tests. This will create `.vscode/settings.json` file in the root that contains the configuration for testing.

1. In the Test Explorer, you will see play buttons next to each test. Click the play button at the top level to run all tests or the button next to each to run them individually.

1. Navigate to the a test file and notice that there is a play button next to each test function signature (name and parameters)
