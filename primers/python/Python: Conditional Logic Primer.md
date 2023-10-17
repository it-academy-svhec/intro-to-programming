# Conditional Logic

## If Statements
If statements are the most basic way to make decisions in Python.

1. Create new Repl called **Conditional Logic Primer**
1. Enter the following source code:

    ```python
    available = True
    
    if available:
        print("Item is available.")
    ```

1. Run the program and notice that the item is available.

1. Change the value of the `available` varaible to `False` and run the program again 

1. Add the following line of code above the `available` variable declaration

    ```python
    name = input("Enter the item name:\n")
    ```

1. Add a line of code inside the if block to print the name of the item

1. Enter the following code after the if block

    ```python
    if not available:
        print("Item is unavailable")
    ```

1. Run the program

Note that this approach can be condensed using the next programming construct.

## If-Else Statements
1. Refactor the previous code to use an if-else statement

1. Instead of hardcoding the value for the variable `available`, prompt the user for a boolean value. You will need to use the `bool()` method to cast the `str` value from the user to the `bool` data type.

1. Run the program. You should now be able to enter the name and availability for an item and then view the results printed to the console.

## If-Elif-Else Statements
Imagine that we have a more complicated series of statuses for an item.

The program needs to support the following statuses:

- Available
- Unavailable
- Sold
- On hold

1. Clear the Repl and enter the following incomplete code

    ```python
    name = input("Enter the item name:\n")

    status = input("Enter the item status (available, unavailable, sold, or on-hold):\n")

    if True:
      print(name, "is available")
    elif True:
      print(name, "is unavailable")
    elif True:
      print(name, "is sold")
    elif True:
      print(name, "is on hold")
    else:
      print(name, "does not have a valid status")
    ```

1. Finish the program by implementing the correct conditional checks where `True` is hardcoded

1. Run the program and test that it works correctly

## (Optional) Match Statements
Recall `switch` statements in the C programming language were a convenient way to avoid countless `else if` blocks. Python doesn't support this exact statement, but version 3.10 released the `match` statement, which is very similar.

1. Refactor the program to use the `match` statement instead. Use this link as reference https://www.geeksforgeeks.org/python-match-case-statement/
