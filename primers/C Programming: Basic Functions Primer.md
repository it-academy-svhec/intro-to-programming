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
