# If-Else Statements Primer

If statements are used to perform an action only if a condition is true. This is a common _selection_ or _branching_ structure since it shifts the direction of the program and is easy to understand. In the absence of this kind of _decision_ structure, programs would always produce the exact same output and flow in one direction. Real-world programs are complicated and require decision making based on conditions of the inputs.

## Basic If Statements
Assume you need to check if a number is positive. We will get the number as input from the user's console (Terminal). If it is positive, the program will print the message `The number is positive`. Otherwise, the program will simply terminate. This program will take two paths: print that the number is positive or do nothing.

Keyword: `if`

1. Create a Repl called **If-Else Statements Primer**

1. Type the following source code and optionally enter the comments

    ```C
    #include <stdio.h>
    
    int main()
    {
      int number = 0;

      // Store a number from the console to the variable called number
      scanf("%d", &number);

      if (number > 0)
        printf("The number is positive\n");

      return 0;
    }
    ```

    Curly braces are not required for the `if` block if there is a single statement under the if keyword. Note that Python programming requires proper indentation, so make a habit of indenting your code early.
    
    This program is very limited since it does not print a message if the number is not positive. The single `if` statement is useful for simple actions, especially when you only care to act if the condition is true. Frequently we need to act when the condition is false as well. This leads to a different direction in which the program can flow.

1. Run the program and test (one at a time) with the following inputs: -1, 0, and 1. Ensure you get the expected results. 

## Handling the False Case - If-Else Statements
Let's enhance the previous program by producing output if the number is not positive (i.e., it fails the condition check).

Keywords: `if` and `else`

1. Add the following line of code after the `printf` statement but at the same level of indentation as the `if` keyword.

    ```C
    printf("The number is not positive\n");
    ```

1. Run the program and test (one at a time) with the following inputs. Confirm the correct outputs are shown.

    |Input|Output|
    |-|-|
    |-1|The number is not positive|
    |0|The number is not positive|
    |1|The number is positive|

1. Note that you should observed the correct outputs for -1 and 0, however, 1 should have resulted in the following. Unfortunately, that is a contradiction. How can a number be positive and not positive simultaneously. Analyze why this is happening in your code.

    ```
    The number is positive
    The number is not positive
    ```

1. Currently, the program prints `The number is positive` if the number if greater than 0. Then it proceeds to run the print statement for `The number is not positive`. Since this statement is not inside an if or else block, it always runs.

1. To fix this problem, move the second print statement into an `else` block as shown below

```C
else
  printf("The number is not positive\n");
```

1. Then test the inputs in the table above. Ensure the program behaves as expected.
