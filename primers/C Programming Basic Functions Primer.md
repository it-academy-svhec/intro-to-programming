## Basic Functions Primer
Functions are provided by the C standard library or can be user defined. Functions are very useful since they allow us to reuse logic and share code with our teammates.

### Using Existing Functions
C standard library functions are imported to a program with the `#include` preprocessor directive. For example, to import the Standard I/O library, you can add `#include <stdio.h>` at the top of your source file. C standard library files are imported using the `<` and `>` syntax. On the other hand, if you have a user-defined file to import, you can write `#include "my_file.h"` to import those custom functions.

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
Now let's define a custom function to raise a number to the 2nd power (also called squaring a number). This custom function will only exist inside our source code file. There are more complex steps to sharing the function in other source code files that we will cover later.

1. Use the Repl from the previous section and clear the source code completely

1. Add the following code:

      ```C
      #include <stdio.h>

      // Function declaration (prototype)
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
      This function takes one parameter (formal argument) called `num` of the type `int`. It returns an `int`.

1. Now call the function and store it in a variable:

      ```C
      int result = 0;
      result = square(10);
      ```

1. Next print the number to the console:

      ```C
      printf("10 squared is %d\n", result);
      ```
