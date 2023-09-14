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
      print_heading("coding");  // Call
    
      return 0;
    }

    // Definition
    void print_heading(char heading[]) { printf("====%s====", heading); } 
    ```

    `void` indicates that this function returns nothing. It does print text but that is not a return value, that simply puts text onto the console.
    Formal parameter is `char heading[]`, which means a character array named `heading`. A character array is a string.

1. Run the code and notice that it prints the heading

1. Modify the function call to take the actual parameter (argument) `programming` and run the program

## Changing the definition

Let's modify this function to capitalize the first letter of the heading

1. Modify the body of this function to the following.

    ```C
    heading[0] = heading[0] - 32;
    
    printf("====%s====", heading);
    ```

    Since `heading` is an array of characters, we can use the `[]` operator to access elements in the array. Each element is of the `character` data type. The first element is at position `0` and accessible via `heading[0]`. Then the second is accessible at `heading[1]` and so on. So `heading[0]` allows us to access the first character in the string representing the heading. Then we set it equal to itself minus 32, which shifts the ASCII value from the lowercase version to the uppercase version. See an ASCII chart online to notice that any lowercase letter such as `a` is 32 places higher than any uppercase letter such as `A`.

1. Run the program and check the output

## Using Return Types

Now let's create a new function to add to the existing program.

1. Create a new function with the following requirements. Add the definition under `main` and the declaration above `main`.

    - Return type: integer
    - Name: `multiply_numbers`
    - Formal parameters: 2 integers
    - Operation: multiply the numbers supplied as arguments and return the product

1. Call the function and print the result

## Recursion

Recursion is useful when you need to run the same function over and over again on slightly different inputs. This process requires a self-referencing function (i.e., the body of the function actually calls itself). This is helpful when roughly the same operation needs to be run on a set of values all related to one another.

Imagine trying to search for a file in a set of folders. 

![image](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/7125726e-e569-4f54-93fa-6011a74f60b3)

We can start with the top-level root folder (C:\). Then `recurse`, or call the search function over and over again. Next we would search in the folders contained in the root folder. Then we would search through the nested set of folders and so on. Each time we are still running the same operations to try to find the file but just working with a different folder.

Unfortunately, it is bit complex to implement file searching in C, so instead let's build a program to do some simple math operations.

In statistics, you often encounter the factorial `!` operator such as `3!`. `3! = 3 * 2 * 1`. We can write a recursive function to compute this.

1. Add another function defined below

    ```C
    int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
    
        return n * factorial(n - 1);    // This line call the function itself on the next lowest number
    }
    ```

1. Call the `factorial` function on the number `3` and print the result

1. Run the program and confirm that it outputs `6` for `3!`

What is happening?

1st function call is `factorial(3);`

    // Evaluates to false, so it does not return 1
    if (3 <= 1) {
        return 1;
    }

    return 3 * factorial(3 - 1);    // Returns the product of 3 and next recursive function call

2nd function call is `factorial(2);`
    
    // Evaluates to false, so it does not return 1
    if (2 <= 1) {
        return 1;
    }

    return 2 * factorial(2 - 1);    // Returns the product of 2 and next recursive function call
    
3rd function call is `factorial(1);`
    
    // Evaluates to true so it returns 1
    if (1 <= 1) {
        return 1;
    }

    return 1 * factorial(1 - 1);    // Doesn't get called

We can evaluate this backwards. The result of the 3rd call is used in the 2nd call. The result of the 2nd call is used in the 1st call.

You can also visualize this as the following chain:

`factorial(3) = 3 * factorial(2)`

`factorial(2) = 2 * factorial(1)`

`factorial(1) = 1` reaches a `base case` or basically a number rather than another function call.

Then you can use the result to work backwards.

`factorial(2) = 2 * 1 = 2`

`factorial(3) = 3 * 2 = 6`

So `factorial(3) = 6`.
