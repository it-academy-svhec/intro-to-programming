# Structs Primer
Structures, or `structs` for short, are used to store many variables and encapsulate data in one place. This allows us to perform operations on an abstract data type (ADT) rather than always working with primitives. ADTs provide very close models of the real world and allow us to focus on the design (high-level understanding) rather than the implementation (nuts and bolts). If you would like to read more about ADTs, check out some course material from [ODU](https://www.cs.odu.edu/~zeil/cs361/latest/Public/adts/index.html),

**Keyword**: `struct`

## Terminology
- Member variable: a variable stored inside a struct
- Member access (dot) operator: denoted by a period (`.`) and used to access member variables

## Defining and Creating Structs
Structs are defined outside of any function. Although the definition of a struct isn't really a statement, it does end with a semicolon (`;`).

1. Create a Repl called **Structs Primer**

1. Enter the following code to create a struct to model time as hours, minutes, and seconds

```C
#include <stdio.h>

struct Time {
  int hours;
  int minutes;
  int seconds;
};

int main(void) {
  // Initialize the struct. Note the values correspond to the member variable positions.
  struct Time start_time = {1, 30, 10};
  struct Time end_time = {5, 45, 5};

  return 0;
}
```

1. Run the program to ensure it is functional

1. Add another variable of the data type Time called `diff_time`, short for difference between times. You do not have to initialize the values since they will each automatically be set to 0.

## Settings and Accessing Member Variables
Member variables that are encapsulated within structs are set and accessed via the dot operator (`.`). The values of the member variables can change throughout the lifetime of a struct just like primitive variables.

1. Under the last struct declaration, add the following print statement to print the value of the member variable `hours` of the struct `start_time`

    ```C
    printf("Start time - hours: %d", start_time.hours);
    ```

1. Under the previous print statement, add two more statements to print `minutes` and `seconds` for `start_time`

## Nested Structs

## Arrays of Structs

## Structs with Array Members
