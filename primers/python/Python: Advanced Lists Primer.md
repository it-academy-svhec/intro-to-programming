# Advanced Lists Primer

## Slicing Lists

1. Create a new Repl called **Advanced Lists Primer**

1. Enter the following source code

    ```python
    items = ["book", "laptop", "xbox", "car"]

    print(items)
    ```

1. Run the program and ensure the items are printed out

1. Create a new list called **some_items** and assign it the first half of the **items** list. Use the list slice technique.

1. Add a print statement to show the items in **some_items**

1. Run the program

## Searching through Lists

1. Create a variable called **last_item** and assign it the value of the last item in the **items** list

1. Write a print statement to show this item

1. Add the following code to prompt the user for an item name

    ```python
    search_item = input("Enter an item name: ")
    ```

1. After that line, add some code to check if the **search_item** is in the **items** list. Print a statement to indicate whether or not the item was found.

## List Comprehensions

1. Enter the following code to capitalize each word in the **items** list

   ```python
   for i in range(len(items)):
     items[i] = items[i].capitalize()
  
   print(items)
   ```

1. Run the program

1. The problem right now is that this changes the **items** list permanently and we don't want to do this. Instead, we would rather print the capitalized version without changing the first list. Convert the previous for loop into a list comprehension and assign if where the comment is defined below.

    ```python
    proper_items = # replace with list comprehension
    ```

1. Change the print statement to print the new list **proper_items**

1. Run your program and notice how much less code there is to accomplish the same task

1. Declare a new list called **copy_items** and assign it a multi-dimensional list with the following structure

    - Each list element will be a list
    - In each inner list there will be two elements: the name of the item and the price
    - You can add any float for each price
    - The list should look like this: `copy_items = [["book", 5.0] ...]`. You will replace `...` with the remaining items
    - Each item is a 2-element array with the name and the price as an float
    - Fill these items out for all 4 items originally declared in the **items** list

1. Implement some code similar to the following to loop over each item and print the name and price. The name and price should be printed using print statements rather than as a result of running `print(copy_items)`

   ```python
   for copy_item in copy_items:
     for # replace this line with code to allow you to loop over the name and price for each item

1. Run the program and confirm that it works as expected
