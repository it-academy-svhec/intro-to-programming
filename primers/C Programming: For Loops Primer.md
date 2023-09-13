# For Loops Primer
These loops are great for iterating a fixed (known) number of times.

**Keyword:** `for`

## Terminology
- **Loop**: structure used to repeat code
- **Iteration**: an execution of the loop. One instance of the loop running.
- **Control variable**: used to track iterations. Incremented or decremented before each iteration.
- **Increment**: add one to the control variable
- **Decrement**: subtract one from the control variable

## Structure

    for (initialization; condition; increment/decrement) {
      body
    }

    For loop is made of statements ending in semicolons except for the increment/decrement statement.

### Components
- **Intialization**: initialize a **control variable** to track the number of loop iterations
- **Condition**: logical condition checked before each iteration. If true, iterate, else, terminate loop and move to next statement.
- **Increment/decrement**: add one to the control variable or subtract one from the **control variable**
- **Body**: contains code to be repeated. One or more statements. Skipped entirely if the condition is false.

## Basic Usage
Let's write a basic for loop that runs a block of code 10 times. It will print the value of the control variable, `i`, on each iteration.

1. Create a new Repl and name it **For Loops Primer**

1. Enter the following source code

    ```C
    #include <stdio.h>
    
    int main(void) {
      for (int i = 0; i < 2; i++) {
        printf("Iteration %d\n", i);
      }
    
      return 0;
    }
    ```
    This loop iterates (runs) 2 times.
    First iteration: starts at i = 0 and ends at i = 1
    Second iteration: starts at i = 1 and ends at i = 2
    Then i = 2, which is not less than 2, so the condition is false and the loop terminates.

1. Modify the loop to run for 10 times

## Loop Based on User Input
User input can be used to affect loops in your code. Recall that `scanf` can be used to gather user input from the console.

1. Clear the Repl

1. Add the following code

    ```C
    #include <stdio.h>
    
    int main() {
        int num;
    
        printf("How many times should the loop run? Enter a positive number below:\n");
    
        scanf("%d", &num);
    
        for (int i = 1; i <= num; i++) {
            printf("%d ", i);
        }
        
        return 0;
    }
    ```

## Using Loops for Linear Search
A linear search a search strategy in which you look through every element in a list until you find the correct one. For example, imagine you are looking through a pile of 100 randomly arranged unique books. Your goal is to find one specific book. If you simply look at each book one by one, then this is a linear search.

Let's try this approach to search through a list of numbers to determine if the list contains a specific number. For loops are great for searches if you know how many elements are in the list.

1. Clear your current Repl

1. Copy and paste the following code

    ```C
    #include <stdio.h>
    
    int main() {
      int numbers[] = {1, -3, 0, 10, 48, 100, -21}; // Define array with 7 integer elements
    
      int search_number = 0; // Define variable to store the number the user is looking for
      int is_found = 0; // Boolean to determine if the number is found in the array
    
      printf("What number would you like to find?\n");
      scanf("%d", &search_number); // Scan console for user input
    
      for (int i = 0; i < 7; i++) {
        // Check if the number is found
        if (numbers[i] == search_number) {
          is_found = 1; // Set to true
    
          printf("Found at position %d\n", i); // Tell user where the number is
          break; // Terminate loop
        }
      }
    
      // If we did not find the number, print message staging not found
      if (!is_found)
        printf("%d not found in array\n", search_number);
    
      return 0;
    }
    ```
    The array `numbers` is initialized with 7 integer elements. We can access an element in an array with the `[]` operator/notation. For instance, to access the first element (0th), you can write `numbers[0]`. The list index starts at zero, so the first element is really at position `0`. We can use the for loop to go through the array of numbers one-by-one. On each loop iteration, we check if current element in the array matches the number we are searching for.

1. Run the program and experiment searching for existent and non-existent values in the array `numbers`

1. Modify the code to include a number of your choice at the end of the array `numbers`. Note the position that you placed the number.

1. Run the program and search for your number. If you are unable to find your number, consider modifying another part of the code to support this functionality.
