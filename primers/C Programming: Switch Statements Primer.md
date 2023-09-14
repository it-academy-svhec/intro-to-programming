# Switch Statements Primer
Sometimes else-if statements with many different branches become unruly and difficult to follow. Switch statements provide a more compact way to handle complex conditional logic.

**Keywords:** `switch`, `case`, `default`, and `break`

## Basic Usage
Let's write a program that reads a student's letter grade from the console input. Then it should print a message indicating whether or not they passed the class.

1. Create a new Repl named **Switch Statements Primer**

1. Copy and paste the following source code

    ```C
    #include <stdio.h>

    int main(void) {
      char grade;
    
      scanf("%c", &grade);
    
      switch (grade) {
      case 'A':
        printf("You passed the class.");
      case 'B':
        printf("You passed the class.");
      case 'C':
        printf("You passed the class.");
      case 'D':
        printf("You passed the class.");
      default:
        printf("You failed the class.");
      }
    
      return 0;
    }
    ```

    The switch statement checks the value of the `grade` character variable against each case. If grade equals the value to the right of the `case` keyword, the code after the `:` colon is executed.

1. Run the program and enter a few grades to test it. Notice anything strange?

1. The program should show the following output, which is probably not what we had intended

    ```
    You passed the class.
    You passed the class.
    You passed the class.
    You passed the class.
    You failed the class.
    ```

    Currenlty, the flow of control is `falling through` to the default case. Instead, we need to execute the code in the correct switch case and then terminate the switch statement. The switch statement is missing the `break` statement. This statement terminates the switch statement once one of the conditions are met.

1. Add the following code after each print statement in the `case` and `default` blocks

    ```C
    break;
    ```

## Leveraging the Fall-Through Behavior
Sometimes it is convenient to utilize the fact that control flows through each case until a break statement is executed. This allows us to trigger one case's code for multiple values for the variable that the switch checks.

1. Clear the current Repl and copy/paste the following source code

    ```C
    #include <stdio.h>

    int main(void) {
      char grade;
    
      scanf("%c", &grade);
    
      switch (grade) {
      case 'A':
      case 'B':
      case 'C':
      case 'D':
        printf("You passed the class.");
      default:
        printf("You failed the class.");
      }
    
      return 0;
    }
    ```

1. Run the program and test with grades A, B, C, D, and F

## Refactoring Switch to Ternary Operator

Oftentimes, switch statements can be refactored with other structures such as the `ternary operator`.

1. Refactor your code to use the ternary operator as shown below.

    ```C
    #include <stdio.h>
    
    int main(void) {
      char grade;
    
      scanf("%c", &grade);
    
      printf(grade >= 'A' && grade <= 'D' ? "You passed the class." : "You failed the class.");
    
      return 0;
    }
    ```

1. Run the program and ensure it still behaves the same

With this approach, the ternary operator checks if the grade is A - D (inclusive). If so, it prints "You passed the class.". Else, it prints "You failed the class.".

## Refactoring the Else-If to Switch
You will rewrite the else-if ATM menu program using a single switch statement.

Tips and strategies:

- Code the switch statement right above the else-if structure
- Move the code over piece by piece. For instance, get the switch statement to work for the first menu option. Then continue and implement the rest of it.
- Test frequently to make sure you are on track

1. Fork the Repl you created previously called **Else-If Statements Primer**

1. Name the new Repl **Refactoring Else-If to Switch Primer**.

1. Refactor the else-if ladder (chain) structure to use one switch statement

1. Test that it still behaves the same

## Takeaways

- Switch statements are used to conditionally execute code based on the value of a variable
- The variable checked is technically treated as an integer (`int` or `char`, which is internally stored as an integer)
- Use switch statements sparingly
- Consider using switch statements when there is a long "ladder" of else-if statements
- The `case x:` is used to denote the block of code that runs when the variable is equal to x
- Control flows through each case until it hits a `break` statement
- Each case should contain a break statement for safety
