## Basic Addition Primer

You will create a C program in Replit that defines a number, adds another number to it, and then prints the result. This primer explores concepts including variables, data types, and arithmetic operations.

### Writing the Program

1. Create a new Repl and call it **Basic Addition Program**
1. You can add comments to your code by typing `//`. Any text after the two forward slashes is considered a comment and is ignored by the compiler
1. Enter the following source code in the Repl line by line. Pay close attention to the syntax and do not just copy and paste the code. 

    ```C
    #include <stdio.h> //
  
    int main(void) {
      int number = 25;
  
      number = number + 15;
  
      printf("My number:\n");
      printf("%d", number);
  
      return 0;
    }
    ```

### Using Other Arithmetic Operators
1. Run the program
1. Let's try changing the operator `+` to each of the following operators. Follow this proces: predict the expected output for the variable `number`, change the operator, run the program, and compare the actual result to the expected result.
    - Subtraction: `-`
    - Multiplication: `*`
    - Division: `/`
1. Try to figure out why some of your predictions were wrong. What do you think is happening?
