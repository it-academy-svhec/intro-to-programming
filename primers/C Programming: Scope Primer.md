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

1. Now the following code directly above the main function. Recall that `void` means the function does not return a value. This function should simply add 10 `number` and store the result in `number.

    ```C
    void add() {
      number += 10;
    }
    ```

    You may find that saving the Repl causes the code to be reformated to appear inline. That is ok and this occurs because the function is just a one-liner at this point.
    Note that we are able to place the entire function definition above the main function. The compiler is able read the `add` function before its first use in the `main` function. Functions must be defined or at least declared (i.e., prototype placed outisde of main) before being called.

1. Note that you should see `number` highlighted in red and an error. Read the error message and ignore this for now.

1. Add the following code after the line that defines `number`

    ```C
    printf("Before calling add function: %d\n", number);
  
    add();
  
    printf("After calling add function: %d\n", number);
    ```

1. Run the program and notice, of course, that the program does not compile. This is due to trying to access `number` which is out of scope in the `add` function.

There are two ways we can resolve this issue.

### Solve Using a Function Argument
The `add` function does not have the access to `number` since `number` is locally scoped to the code block for `main` (i.e., the left and right braces for main). The right and left braces for the `add` function denote another scope entirely that is local to that function. We can pass the `number` variable defined in `main` into the `add` function as an argument.

1. Change the signature of the add function to `add(int number)`. Now the function can accept an argument called `number`.

1. Change the part where you call `add` from `add();`, which has no arguments to, `add(number)`, which has one argument.

1. Note that the value of `number` is still the same before and after we call the `add` function. That is because when `number` is passed into the `add` function we are actually receiving a copy, not the real variable.

In the next section we will address a different of solving this issue with global variables.

## Global Scope
External or global scope means that the variable is accessible anywhere in the C program (*.c) file. This is not generally necessary but can be useful when variables need to be shared by multiple functions including `main`. Global variables are declared outside of code blocks (pairs of braces). This is very useful for situations such as in the previous example where we need to change a variable's value inside a function.

1. Move the line of code that defines `number` one line above the main function

1. Now change the implementation (body) of the `add` function to add `number` and `global_number`. You do not need to change the parameters/arguments passed into the function.

1. Run the program

You had to pass `number` as an argument to `add` since it was locally or block scoped. On the other hand, you were able to access `global_number` inside the `add` function without passing it as an argument since it is globally scoped.
