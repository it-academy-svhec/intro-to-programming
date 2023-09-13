# While Loops Primer
While loops are typically used when you don't know how many iterations should be performed. On the other hand, for loops are good when the number of iterations is known.
These loop structures are a great choice for gathering user input. While loops can keep programs running until an exit signal is specified by the user.

**Keyword:** `while`

## Basic Usage

Let's create a basic loop that reads a number from a user. The loop should continue if they enter a number between 1 and 100 (inclusive).

1. Create a Repl named **While Loops Primer**

1. Enter the following source code

    ```C
    #include <stdio.h>
    
    int main(void) {
      int number = 0;
    
      while (number >= 0 && number <= 100) {
        printf("To continue, enter a number between 0 and 100:\n");
        scanf("%d", &number);
      }
      return 0;
    }
    ```

1. Run the program with the following inputs to test the correctness of the code: -1, 0, 1, 99, 100, and 101

## Avoiding Infinite While Loops
If the while loop's condition never evaluates to false, the loop will run forever.
Let's create a while loop that runs infinitely.

1. Replace the body of the main function with following source code

    ```C
    int i = 0;
    
    while (1) {
      printf("%d\n", i);
    
      i++;

      // Emergency brake if loop appears to be infinite
      if (i > 1000)
        break;
    }
    ```
