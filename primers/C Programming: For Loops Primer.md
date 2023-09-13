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
      for (int i = 0; i < 10; i++) {
        printf("Iteration %d\n", i);
      }
    
      return 0;
    }
    ```
