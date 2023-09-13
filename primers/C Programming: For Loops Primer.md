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

Let's try this approach to search through a list of numbers to determine if the list contains a specific number. For loops are great for searches if you know how elements are in the list.

1. Enter the following code
