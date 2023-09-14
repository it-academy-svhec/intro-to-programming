# Scope Primer

## Block Scope
Block scope means that a variable is only accessible inside of the code block in which it is defined. A code block is denoted by a `{` (left brace) and `}` (right brace). Anything inside the associated braces is part of the same code block and therefore has the same block-level scope. Code blocks are used to group related code such as in functions, if statements, for loops, and while loops. Contains `automatic` or `local` variables whose scope is contained to a specific code block.

1. Create a new Repl called **Scope Primer**

1. Enter the following source code

    ```C
    #include <stdio.h>
    
    int main() {
      int number = 2;
    
      return 0;
    }
    ```
    This code defines an integer variable `number` set to `2`. The variable is locally-scoped, which means that it is only accessible within the body of the `main` function.

1. Now the following code directly above the main function

    ```C
    int add(int number) {
      return number + 10;
    }
    ```

    You may find that saving the Repl causes the code to be reformated to appear inline. That is ok and this occurs because the function is just a one-liner at this point.
    Note that we are able to place the entire function definition above the main function. The compiler is able read the `add` function before its first use in the `main` function. Functions must be defined or at least declared (i.e., prototype placed outisde of main) before being called.

1. Run your program just make sure you don't have any errors. For now, it will not output anything.

1. Add the following code after the line that defines `number`

    ```C
    printf("Before calling add function: %d\n", number);
  
    add(number);
  
    printf("After calling add function: %d\n", number);
    ```

1. Run the program and notice that the value of `number` does not change. That is because the `number` variable declared inside the `main` function is only accessible to `main`, not the `add` function. When you called the add function with `add(number)`, the function gets a copy of the value stored in `number`. When we add 10 to the number inside the `add` function, we are working with another variable called `number` with scope local to the `add` function. In other words, the `number` variable in `main` is not the same as the `number` variable in `add`. They are different and only exist in their respective code blocks.

## Global Scope
External or global scope means that the variable is accessible anywhere in the C program (*.c) file. This is not generally necessary but can be useful when variables need to be shared by multiple functions including `main`. Global variables are declared outside of code blocks (pairs of braces).

1. Add the following line outside of the main function before the `add` definition

    ```C
    int global_number = 20;
    ```

1. Now change the implementation (body) of the `add` function to add `number` and `global_number`. You do not need to change the parameters/arguments passed into the function.

You had to pass `number` as an argument to `add` since it was locally or block scoped. On the other hand, you were able to access `global_number` inside the `add` function without passing it as an argument since it is globally scoped.
