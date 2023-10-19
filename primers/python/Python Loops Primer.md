## Loops Primer
Loops are a programming structure that allow repeating code until a specific condition is met. They are useful for iterating through lists of strings, integers, and objects such as users in a database. Python supports `for` and `while` loops.

## While Loops
While loops are very useful for running the main control loop in a program. They are good for collecting user input that needs to be validated. In general, you should use a while loop when do not know the exact number of times the loop should iterate.

1. Fork the Repl from the **Conditional Logic Primer** and call the new Repl **Loops Primer**

1. Place the existing code conditional logic primer inside the following loop

  ```python
  valid_status = False
  while not valid_status:
      # Replace with existing code from conditional logic primer
      if status == "available" or # Finish the code:
        valid_status = True
  ```

1. Finish the missing part of the if statement inside the while loop. The `valid_status` variable should only be set to `True` if the status entered is one of the valid statuses used later in the program.

1. Run the program and test with valid and invalid statuses

## For Loops
For loops are useful when the number of iterations is known upfront. For example, if you have a list of 10 strings and want to display all of them, a for loop is the best choice. You will simply set up the for loop to run 10 times and on each iteration print the corresponding element in the list.

1. Enter the following line of code above the `name` variable declaration
  
    ```python
    statuses = ["available", "unavailable", "sold", "on-hold"]
    ```

1. Now, make the following changes below

    Old code
    ```python
    status = input("Enter the item status (available, unavailable, sold, or on-hold):\n")
    ```
  
    New code
    ```python
    print("Enter the item status\n")
    print("Choose from the following options:")
    
    for i in range(4):
        print(statuses[i])
    
    status = input()
    ```
    This code prints all defined item statuses. Then it collects the user input and stores it in the `status` variable.
  
1. Run the program

1. Now refactor the `for` loop using the following form

    ```python
    for status in statuses:
        print(status)
    ```

1. Run the program and notice that it functions the same way but is much easier to read
