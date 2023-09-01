## Basic Functions Primer

### Using Existing Functions
1. Create a new Repl called **Basic Functions**
   
1. Enter the following source code and run the program
      ```C
      #include <stdio.h>
      
      int main(void) {
         printf("%s", "Hello!");
      
         return 0;
      }
      ```
      `printf` is a function supplied by the built-in Standard I/O (Input/Output) library. This is imported via the `#include <stdio.h>` statement at the top.

      For tons of built-in functions, check out [C library functions](https://www.geeksforgeeks.org/c-library-functions/).

1. Add the following line of code above the current include statement to import time functions

      ```C
      #include <time.h>
      ```

1. Now call the function named `time` and print the result

### Defining Custom Functions
Now let's define a custom function to raise a number to the 2nd power (also called squaring a number).

1. Use the Repl from the previous section

1. Add the following code:

      ```C
      #include <stdio.h>

      // Function prototype
      int main(void) {
         // Store the result of the function called on the number 10

         // Print the result of raising 10 to the 2nd power
               
         return 0;
      }

      // Function definition
      ```
      Comments are denoted with `//`. Replace each comment line with the appropriate code.

1. Add the following code for the function definition:

      ```C
      int square(int num) {
         int result = num * num;

         return result;
      }
      ```

1. Add the function prototype so the compiler knows that the function is defined later in the code:

      ```C
      int square(int num);
      ```

1. Now call the function and store it in a variable:

      ```C
      int result = 0;
      int result = square(10);
      ```

1. Next print the number to the console:

      ```C
      printf("10 squared is %d\n", result);
      ```
