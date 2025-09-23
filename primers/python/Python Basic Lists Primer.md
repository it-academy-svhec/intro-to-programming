# Basic Lists Primer
Lists are multi-value variables in Python used to store many different values. They can store values of different data types unlike compiled languages such as C, C++, and Java. These data structures are essential to prevent repetitive declarations of similar variables. For example, if you have 10 user accounts each with a first name, last name, and phone number, it would be very tedious to store these values using variables.
In fact, you would need 30 individual variables. Lists are very efficient because you store many values and reference the list as a single variable. 

## How to do this primer
You will use these instructions to build a Python script step-by-step in a separate file. Each step either provides exact code to type into your file or instructions on how to write the code. By the end of the primer, you should have a fully functional Python script.

## Terminology
- **List:** multi-value variable store storing many values
- **Element:** an individual value stored in a list
- **Index:** a number that represents the position of an element in a list. Must be a positive or negative integer. Starts at zero and ends at one less than the length of the list.
- **Length:** the number of elements in a list
- **Append:** add an element to the end of a list
- **Insert:** add an element to the list at a specific index
- **Access operator:** pair of square brackets with numeric index inside

## Creating Lists
First, you need to know how to define a new list. New lists can be declared with default values or they can be empty. Assume that we need to store users' first names.

1. Create a new Python file

1. Create an empty list named `users` by entering the following code

    ```python
    users = []
    ```

1. Add a print statement below the declaration of the users list to print the contents

    ```python
    print(users)
    ```

1. Run the program and notice that `[]` is printed. This formally indicates that the list is empty.

1. Change the declaration of the users list to initialize it to have 3 elements. Notice how each element is separated by a comma and wrapped in quotes since they are strings.

    ```python
    users = ["Linus", "Ada", "Rose"]
    ```

1. Run the program again and notice that the names are printed. They are shown in square brackets and in single quotes because we printed the entire list data structure.

1. Now let's make it look nicer for the end user. Remove the current print statement. Add a print statement for each element in the list.

   ```python
   print(users[0])
   print(users[1])
   print(users[2])
   ```
   Note the index used on each line. It starts at 0 for the first element, then 1 for the second element, and finally 2 for the third and last element.

1. Run the program and notice that it now shows each user's name on a separate line. Using the print statement directly on a list is good for debugging but not for displaying output nicely for a user.

## Storing and Accessing Elements

Next, we need to modify the elements in the users list.

1. Above the print statements, add the following line to add a new user to the list. Replace the empty string (`""`) with your first name.

    ```python
    users.append("")
    ```
    The `append` method operates within the context of the list on the left of the dot operator. It adds the argument in the parentheses to the end of the list.

1. Then add a print statement to print your name from the list in the same way the other print statements are being used

1. Let's add another name to the list but this time place it as the first element of the list. Add the following line of code right after the append statement. Replace the empty string with a classmate's first name.

    ```python
    users.insert(0, "")
    ```
    The `insert` method also works in the context of a list. It places the argument in the parentheses in the list at the specified index. In this case, the index is `0`, which is the first position in the list.

1. Run the program and notice that the value passed to the `insert` method is now the first element. The last element of the list should also be missing from the printed output.

1. Write a line of code to print the last element of the list

## Deleting Elements

We often need to delete elements in lists. You can use the `del` instruction or the `remove` list method to acheive this goal.

1. Remove the first element in the list by adding the following line of code after the print statements

    ```python
    del users[0]
    print()
    print(users[0])
    ```
    `del` is a global instruction that deletes the element in a specified list at the given index.

1. Run the program again and notice how the first element printed by index `0` is the element that was previously at position `1`

1. Alternatively, you can delete an element with the `remove` method. Add the following under the last print statement to remove the first element equal to `Ada`.

   ```python
   users.remove("Ada")
   print()
   print(users)
   ```
   The `remove` method checks for an element equal to the argument and deletes the first occurrence of it from the list.

## Updating Elements

The next major task for lists is updating existing elements.

1. Update the element that contains your first name using the following code. Place it at the end of the current program. Replace `<int>` with the index of your first name in the list. Replace the empty string with your first and last name. E.g., "Linus Torvalds".

   ```python
   users[<int>] = ""
   print(users[<int>])
   ```

1. Run the program and you should see your first and last names printed out

1. You can also use the `index` method to find the index of a specific element in a list. Refactor the code above to update your name using the following syntax. Replace the first empty string with your first name. Replace the second empty string with your first and last names like before.

   ```python
   index = users.index("")
   print(f"Name at index {index}")
   users[index] = ""
   print(users[index])
   ```

1. Run your program to ensure it works as expected

## Looping Through Lists

You often have to access all or many of the elements in a list and it is too tedious to use the index in square for element on a single line. It is more efficient to use loops to iterate through a list.

1. Replace the block of 3 print statements at the top with the following for loop

    ```python
    for i in range(len(users)):
        print(users[i])
    ```
    Note that `i` is a variable that gets the value from the `range` function on each iteration. The `len` function computes the length of the list called `users`. So really this is the same as `range(5)`, which generates the number sequence 0, 1, 2, 3, and 4. But writing it this way means that we are not hardcoding the length of the list and it can change freely as new elements are added. This leads to dynamic behavior within our code.

1. Run the program and it should behave in the same way

1. Refactor the for loop to use an even cleaner syntax

    ```python
    for user in users:
        print(user)
    ```
    Now, the details of the index are hidden from us and Python takes care of the low-level details. On each loop iteration, we simply get a user variable set to the element at the current index in the `users` list. Basically, we loop over each user in the list.

1. Run the program and ensure it works as expected
