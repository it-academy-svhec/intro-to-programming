# Operators and Expressions Primer
In this primer, you will work with operators and expressions. Many of these concepts are the based on basic mathematics and can be found in many programming languages from C to Python. Operators, operands, and expressions are all very closely related concepts. First, we will provide a brief conceptual overview. Next, you will work through some basic examples that use all of these concepts together.

## Operators and Operands
- **Operators:** symbols that perform operations with one or more values. `+`, `-`, `*`, and `/` are the basic operators for arithmetic in C and many other languages
- **Operands:** the formal terms for the values used by operations. For example, consider `number1 + 5`. The addition operator is being used in combination with the operands of `number1` and `5`.

## Expressions
Expressions, like in mathematics, are combinations of operations and values that result in new values. For example, `1 + 1` is an expression in basic arithmetic that evaluates to the value of `2`. Expressions can also be combined together like `(1 + 1) * (2 * 3)`. First you evaluate each expression: `2 * 6`. Then you evaluate the new expression formed by the other two, which results in `12`. This systematic approach is also used to interpret expressions in programming languages.

In summary, operands represent the data you work with, operators represent the actions you can take on the data, and expressions are the combination of many operators and operands to create new data.

## Practical Examples

1. Create a new Repl named **Operators and Expressions Primer**

1. Enter the following source code

    ```c
    #include <stdio.h>
  
    int main(void) {
       int num1 = 10;
       int num2 = 2;
  
       printf("Addition: %d", num1 + num2);
       // Todo #1: implement subtraction print statement with num1 and num2
       // Todo #2: implement multiplication print statement with num1 and num2
       // Todo #3: implement division print statement with num1 and num2
  
       return 0;
    }
    ```
    `num1 + num2` is an expression. `+` is the addition operator, which operates on two operands: `num1` and `num2`. Notice that the operands are actually variables, not raw data. We could also have hardcoded teh values as `10 + 2`, but then we would have to change the numbers in many different places. Variables help keep your code organized and reduce the number of changes required when updating code.

1. Complete the 3 TODO items by writing C code. You should also modify the statements to appear on separate lines in the console when the program is run.

1. Run the program and ensure the output is correct and prints on separate lines

1. Add the following lines of code under the last line before the return line of code

    ```c
    int counter = 0;

    printf("Value of count: %d", counter);

    counter++;

    printf("Value of count: %d", counter);
    ```
    The `++` operator incremented the value of the `counter` variable by one.

1. Run the program and you should observe that the value increases by one

1. Modify your code to decrement the value of `count` instead of incrementing it

1. Run the program and ensure you see the correct results

1. Add the following lines of code under the most recent line you added

    ```c
    int selection = 0;
    char result;
    
    result = selection == 1 ? 'Y' : 'N';

    printf("Selection: %c", result);
    ```
    Assume there is a program that supports a menu from which a user can select "Yes" or "No". Since we haven't really shown you how to use strings, we will stick with integers and chars. We want to check the user's input against the value of `1`, which represents true. The ternary operator allows us to set the `result` value to `Y` or `N` depending on the value of `selection`.

1. Run the program

1. Now, modify the program to print out the character `Y`
