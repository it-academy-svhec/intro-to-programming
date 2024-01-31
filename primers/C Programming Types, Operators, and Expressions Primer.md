# Types, Operators, and Expressions Primer
In this primer, we will explore data types, operators, and expressions. You will create a single Replit and use it throughout this primer. Pay close attention to the instructions since there are instances where you will need to partially modify the code or completely clear it.

## Data types

Data is stored in memory as ones and zeroes. So whether you are storing a character for a letter grade or an integer for the number passed, the data is still binary. We use data types to indicate how we should handle stored binary information. Essentially, we can tag the raw binary data to indicate how it should be handled (e.g., as a number, string of text, or single character). C provides basic data types called primitive data types. More complex data types can be constructed from combined the simple primitive data types.

### Integers

The integer data type is used to store positive or negative whole numbers including zero. This data type is useful for storing information such as the number of days in a week or the quantity of a product in stock.

1. Create a REPL named **Types, Operators, and Expressions Primer**

2. Add the following code to define a main program and an integer variable named `days` to store the number of days in a week.

   ```c
   #include <stdio.h>

   int main(void) {
      int days = 7;
   
      printf("Days in a week:\n");
      printf("%d", days);
   
      return 0;
   }
   ```
   `%d` is a format specifier, or placeholder, for the `days` integer data type variable. When the statement runs, the placeholder is replaced with the actual value of `days`, which is an integer.
   
4. Run the program and observe the text ouput

5. Remove the two `printf` statements and enter a the following single `printf` statement to print `There are 7 days in a week.`

   ```c
   printf("There are %d days in a week", days);
   ```
   Placeholders can be added inside a string surrounded by double quotes. The second argument, `days`, is placed where the `%d` placeholder is in the string.
   
   You can add as many placeholders and corresponding actual values as you want. For example, you would write `printf("%d %d %d", 1, 2, 3)` to print the string `1 2 3` to the console.
   Note that the number of placeholders and values should match. 

7. Run the program

8. Clear the program source code and enter the following code instead

   ```c
   #include <stdio.h>

   int main(void)
   {
       int number1 = 10;
       int number2 = 82;

       // TODO #1: multiple the numbers and store in a variable named number3
   
       // TODO #2: print the statement "10 * 82 = 820"
   
       return 0;
   }
   ```

9. Implement the code missing for TODO #1 and TODO #2

10. Run the program

11. Change the values of `number1` and `number2` and rerun your program

### Characters
Characters are stored in a program using the integer data type and use the ASCII encoding scheme. This data type is often used to store data in an abbreviated format. For instance, you may have a list of menu options presented to a user. Instead of the user having to type the exam function they want to select, they could choose from a list of options: A, B, C, etc. It is also useful for storing letter grades such as A, B, C, D, and F and statuses such as E for enrolled and W for withdrawn.

1. Add the following lines of code after the print statement in the current program

   ```c
   char letter_grade = 'A';
   ```
   This declares a new variable of the character data type and initializes it to the value A. Notice that the letter A is surrounded in single quotes (double quotes would denote a string instead).

2. Print this letter grade in a message "Your letter grade is A" using the `printf` function and the `letter_grade`'s actual value. Do not hardcode the value A. If the variable changes, so should the output of the program without the need to change the print statement itself. Use `%c` as the placeholder.

3. Run your program and ensure that you see the expected output. Debug your code if necessary. If your text is running together, you may need to use the `\n` newline character in your print statement.

4. Change the placeholder from `%c` to `%d`

5. Rerun your program. Do you see the expected output? Why or why not? Hint: take a look at this [ASCII chart](https://www.rapidtables.com/code/text/ascii-table.html)

The reason a number is printed instead is because the format specifier `%d` tell the print statement to handle the output as an integer. Characters are internally stored as integers with that correspond to the associated ASCII character.

### Floating Point Numbers
It is easy for computers to store integers, but more complex to store floating point (i.e., decimal numbers) numbers. The underlying binary representation is not 100% precise and takes more memory to store floats. Floats are used for storing values such as financial currency, scientific measurements like temperatures, and percentages used in other calculations. You only want to use floating point numbers when 
absolutely needed because they take more memory and can lead to imprecise results depending on the desired decimal points of precision.

#### Scenario
Imagine you receive a complaint from an accountant that uses your payroll software. They report that employees certain employees are receiving less money in each paycheck than expected. For the sake of simplicity, assume the hourly rate is hardcoded as $15.75.

#### Source Code
1. Add the following lines of code after the last print statement in your program

   ```c
   int hourly_rate = 15.75;
   printf("Your hourly rate is %d", hourly_rate);
   ```

2. Run the program and then try to figure out why it is incorrect

3. Change the data type of `hourly_rate` to `float` and the placeholder of `%d` to `%f`.

4. Once you have fixed the program, rerun the program.

5. Add a variable to store the number of hours the employee works weekly. Set it to 40.

6. Then add a print statement to print the weekly wage of the employee.

### Constants
If you have variable that should not change in value, you can add the keyword `const` in front of the data type.

1. Modify your code to make `hourly_rate` a constant

2. Then try to change the value later in the code with a statement such as `hourly_rate = 16.00;`

3. Run your program and notice that it fails to compile and you see an error message

4. Revert the change in step 2

## Expressions
Expressions, like in mathematics are combinations of operations and values that result in new values. For example, `1 + 1` is an expression in basic arithmetic that evaluates to the value of `2`. Expressions can also be combined together like `(1 + 1) * (2 * 3)`. First you evaluate each expression: `2 * 6`. Then you evaluate the new expression formed by the other two, which results in `12`. This systematic approach is also used to interpret expressions in programming languages.

### Operators and Operands
- Operators: symbols that perform operations with one or more values. `+`, `-`, `*`, and `/` are the basic operators for arithmetic in C and many other languages
- Operands: the formal terms for the values used by operations. For example, consider `number1 + 5`. The addition operator is being used in combination with the operands of `number1` and `5`.
