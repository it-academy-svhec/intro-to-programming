===== Under Construction ======
# Advanced Functions Primer
We use functions primarily to make our code reusable and more readable. Developers can write functions to solve difficult problems and then allow their teammates to use the functions without understanding the low-level implementation details. Functions also help make code more readable when named properly. A complex set of steps can be broken into many functions, each with a descriptive name and specific purpose.

## Terminology
- **Signature**: unique identifier for a function consisting of the function's return data type, name, and expected parameters
- **Declaration/prototype**: the signature of the function placed somewhere outside of main before the function is actually used. This informs the compiler that the function exists somewhere in the code.
- **Body**: code block for a function contained within the curly braces. Contains code to be executed when the function is invoked.
- **Definition**: signature and the body of the function
- **Call/invocation**: the act of running a function
- **Caller**: the function that calls another function
- **Return type**: the expected data type of values to be returned by the function
- **Return statement**: `return` keyword followed by an expression that returns a value to the caller of the function
- **Formal parameter**: a parameter expected by the a function identified by its data type and name
- **Argument (actual parameter)**: data that is actually passed into the function at the time of invocation. Placed in the same position with the corresponding formal parameter.

## Creating New Functions

1. Create a new Repl called **Advanced Functions Primer**

1. Enter the following source code. You can optionally enter the comments.

    ```C
    #include <stdio.h>
    
    void print_heading(char heading[]);  // Declaration
    
    int main() {
      print_heading("Intro to Computer Programming");  // Call
    
      return 0;
    }

    // Definition. Formal parameter is `heading` which is a character array (string)
    void print_heading(char heading[]) { printf("====%s====", heading); } 
    ```

1. Run the code and notice that it prints a heading
