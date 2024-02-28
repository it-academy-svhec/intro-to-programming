# Python Modules 2.1 and 2.2 Primer

## Setup
Create a new Repl with the Python template named `Python 2.1 and 2.2 Primer`.

## Using the Print Statement
The `print()` function is one of the simplest functions in Python and prints output to the command line.

1. Enter the following code into your Repl

    ```python
    print('Hello World!')
    ```
    String values in Python are enclosed by quotes.
   
1. Run the script

1. Now replace the single quotes (apostrophes) with double quotes

1. Run the script again and it should produce the same output. You should use single quotes when dealing with string literals (the exact value of string is known upfront, 'hello'). Use double quotes when the enclosed string might contain single quotes.

1. Add a line of code to print your name. Run the program and you should see both strings on different lines. Notice how the print function automatically inserted a newline after the string you entered.

1. Modify the first print statement to insert a newline character (`\n`)

    ```python
    print('Hello World!\n')
    ```

1. Run the script and ensure there is a an extra newline between the strings

1. Now let's modify the script to print the string `"Hello World!"`. In order to print characters that are normally seen by the interpreter as part of the syntax, we escape them. The backslash `\` symbol allows us to escape from the normal interpretation of a character in the language and have it be the literal string value. Add `\"` at the front and back of the string but within the single quotes.

1. Run the script and ensure that you see the expected text

## Primitive Data Types
Python supports serveral primitive data types including the following

- String: `str` Store strings of characters. Text data.
- Integer: `int` Store whole numbers that are negative, zero, or positive.
- Floating point: `float` Store numbers with decimal places.
- Boolean: `bool` Store True/False values to indicate logical relationships.

1. In the same script, enter the following code under the print statement. Run the script.

    ```python
    message = 'This is a string'
    print(message)
    ```
    The message variable dynamically gets the data type of `str` string

1. You can check the data type of a variable by using the `type()` function

1. Modify the print statement to the following to show the data type of the `message` variable

    ```python
    print(message, type(message))
    ```

1. Run the script and it should print the string as well as show the data type

1. Now create variables for `int`, `float`, and `bool`. Then print their values and their data types using the same method above. Note that you can use `True` or `False` for the `bool` data type.

## Literal values

## Formatted String Literals (F-Strings)

## Logical Operators
- or
- and
- not

## Assignment vs. Equality Operator
- Assignment operator: `=` assign the value on the right to the variable on the left
- Equality operator: `==` check if two values are equal to each other

## Type Safety
Programming languages support data types in different ways. The feature of a programming language to enforce stability of data type choices for variables is called type safety. In type safe languages, like C (for the most part), if you declare a variable with a specific data type, the values assigned to the variable must be of the same data type. Languages that exhibit this behavior are often referred to as "strongly typed." Languages that allow values of different data types to be assigned throughout the lifecycle of a variable are often said to be "weakly typed."

In the case of compiled languages, data types are checked at compilation (compile time). Errors related to misuse of data types for variables are easily caught by the compiler. Languages that do this are have static typing because data types don't change after the compiler produces machine code. Due to this behavior, compiled languages are generally thought to be safer and more stable. Note that languages like C do allow mistakes to be made with pointers and type casting, so you could use the language in a weak, unsafe manner.

Dynamic languages, such as Python, check data types during runtime. If you make a mistake related to the values of incompatible data types in Python, you will find while the end-user is running the program. In a compiled language, you would have noticed this problem before the program finished compiling and therefore before the customer used the program.

Python is extremely flexible with regard to data types and this is both a blessing and a curse. How do you mitigate mistakes in a dynamic language? Test, test, and test again! Consider using test-drive development (TDD).
