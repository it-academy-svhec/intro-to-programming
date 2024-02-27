# Python Modules 2.1 and 2.2 Primer

## Using the Print Statement
- single quotes
- double quotes
- newline
- escaping strings
- positional vs keyword args
- print separator

## Primitive Data Types
- str
- int
- float
- bool
- using underscores as a separator

## Literal values

## Formatted String Literals (F-Strings)

## Logical Operators
- or
- and
- not

## Equality Operator
- ==

## Type Safety
Programming languages support data types in different ways. The feature of a programming language to enforce stability of data type choices for variables is called type safety. In type safe languages, like C (for the most part), if you declare a variable with a specific data type, the values assigned to the variable must be of the same data type. Languages that exhibit this behavior are often referred to as "strongly typed." Languages that allow values of different data types to be assigned throughout the lifecycle of a variable are often said to be "weakly typed."

In the case of compiled languages, data types are checked at compilation (compile time). Errors related to misuse of data types for variables are easily caught by the compiler. Languages that do this are have static typing because data types don't change after the compiler produces machine code. Due to this behavior, compiled languages are generally thought to be safer and more stable. Note that languages like C do allow mistakes to be made with pointers and type casting, so you could use the language in a weak, unsafe manner.

Dynamic languages, such as Python, check data types during runtime. If you make a mistake related to the values of incompatible data types in Python, you will find while the end-user is running the program. In a compiled language, you would have noticed this problem before the program finished compiling and therefore before the customer used the program.

Python is extremely flexible with regard to data types and this is both a blessing and a curse. How do you mitigate mistakes in a dynamic language? Test, test, and test again! Consider using test-drive development (TDD).
