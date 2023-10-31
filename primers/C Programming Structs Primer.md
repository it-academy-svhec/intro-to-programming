# Structs Primer
Structures, or `structs` for short, are used to store many variables and encapsulate data in one place. This allows us to perform operations on an abstract data type (ADT) rather than always working with primitives. ADTs provide very close models of the real world and allow us to focus on the design (high-level understanding) rather than the implementation (nuts and bolts). If you would like to read more about ADTs, check out some course material from [ODU](https://www.cs.odu.edu/~zeil/cs361/latest/Public/adts/index.html),

**Keyword**: `struct`

## Terminology
- Member variable: a variable stored inside a struct
- Member access (dot) operator: denoted by a period (`.`) and used to access member variables

## Defining and Creating Structs
Structs are defined outside of any function. Although the definition of a struct isn't really a statement, it does end with a semicolon (`;`). For simplicity, we will model start and end times as hours, minutes, and seconds. For example, if it is 1:30:40 AM, we would store `1 hour`, `30 minutes`, and `40 seconds`. This is a simplistic model that is useful to demonstrate the power of structs for modeling complex data types.

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

      // We can also use the dot operator to explicitly define member variables assignments
      // Notice how the order does not matter since we have provided the names for each member variable
      struct Time end_time = {
        .seconds = 30, 
        .minutes = 45,
        .hours = 5
      };
    
      return 0;
    }
    ```

1. Run the program to ensure it is functional

1. Add another variable of the data type Time called `diff_time`, which is short for the difference between times. You do not have to initialize the values since they will each automatically be set to 0.

## Settings and Accessing Member Variables
Member variables that are encapsulated within structs are set and accessed via the dot operator (`.`). The values of the member variables can change throughout the lifetime of a struct just like primitive variables.

1. Under the last struct declaration, add the following print statement to print the value of the member variable `hours` of the struct `start_time`

    ```C
    printf("Start time - hours: %d\n", start_time.hours);
    ```
    The period (`.`) after `start_time` allows us to access member variables defined inside the struct `Time`. `start_time.hours` accesses the value of the member variable `hours` inside the struct variable named `start_time`.

1. Under the previous print statement, add two more statements to print `minutes` and `seconds` for `start_time`

1. Add code to print the hours, minutes, and seconds of `end_time`

1. Now we want to calculate the difference between `end_time` and `start_time`. This operation is defined by calculating the difference between each member variable (i.e., hours, minutes, and seconds). We need to subtract the times to figure out how much time has passed since the `start_time`.

    ```C
    diff_time.hours =  // TODO
    diff_time.minutes = // TODO
    diff_time.seconds = // TODO
    ```

1. Print the hours, minutes, and seconds for `diff_time`

1. Run the program and your output should be similar to the following

    Diff time - hours: 4
    Diff time - minutes: 15
    Diff time - seconds: 20

## Nested Structs
You can nest structs inside other structs. For example, we can represent the abstract concept of an event by composing this object of two times: start time and end time.

1. Define a new struct with the following characteristics. Place this definition under the `struct Time` definition.

    - Name: `Event`
    - Member variables:

      | Name | Data Type |
      | - | - |
      |`start_time` | `Time` |
      |`end_time` | `Time` |

1. Define an `Event` variable called `the_event` above `start_time`

1. Refactor the `start_time` variable to be a member variable of `the_event`

  **Old code**
  
  This line creates a new `Time` struct, which is scoped to the `main` function.
  
  ```C
  struct Time start_time = {1, 30, 10};
  ```
  
  **New code**

  This line still creates a struct with the same data, however this one is nested inside `the_event` struct. We have to use the dot operator to access `start_time`. In the previous approach, the struct was in `main` and was not nested. `(struct Time)` explicitly casts the initial values `{1, 30, 10}` to the `Time` struct data type.
  
  ```C
  the_event.start_time = (struct Time){1, 30, 10};
  ```

1. Refactor `end_time` in a similar way

1. Refactor all references to `start_time` and `end_time` to include the `the_event.` prefix

   For example,

   ```C
   printf("Start time - hours: %d\n", start_time.hours);
   ```

   would change to

   ```C
   printf("Start time - hours: %d\n", the_event.start_time.hours);
   ```

1. Run your program and ensure it is error free

## Arrays of Structs
Next, you will finish implementing a program that creates events with start and end times. Most of the program is complete including the following functions:

| Function Name | Purpose |
|-|-|
|`print_time`|Print the hours, minutes, and seconds for a time struct|
|`print_event`|Print a list of events and corresponding start and end times|
|`print_diff_time`|Print the time elapsed between two times|
|`create_time`|Prompt a user for a new time and return a Time struct|
|`create_event`|Prompt a user for a new event and return an Event struct|

Although this is a complex program, you only have to implement three pieces of functionality:

- **TODO #1:** Declare an array of Event structs. It should be capable of storing a number of events equal to the integer `MAX_EVENTS`
- **TODO #2:** Write a for loop to create a number of events equal to the integer `MAX_EVENTS`. Within each loop iteration, you shoudl store a new event in the array.
- **TODO #3:** Print the event referrenced by the current loop index

1. Clear the Repl

1. Copy and paste the code from [Structs Primer Starter Code](https://replit.com/@JacobCook2/Structs-Primer-Starter-Code#main.c)

1. Run the program. Notice that the events are empty for now

1. Implement the code required to complete the todo tasks

1. Run your code and you be able to run through it similar to the following example with these select outputs

        Please create 3 event(s)
        
        Create the start time
        Enter the hours(s):1
        Enter the minutes(s):0
        Enter the seconds(s):0
        
        Create the end time
        Enter the hours(s):2
        Enter the minutes(s):30
        Enter the seconds(s):30
        
        
        Create the start time
        Enter the hours(s):3
        Enter the minutes(s):45
        Enter the seconds(s):0
        
        Create the end time
        Enter the hours(s):5
        Enter the minutes(s):0
        Enter the seconds(s):0
        
        
        Create the start time
        Enter the hours(s):6
        Enter the minutes(s):30
        Enter the seconds(s):0
        
        Create the end time
        Enter the hours(s):8
        Enter the minutes(s):45
        Enter the seconds(s):30
        
        Showing Events:
        Event[0]:
        Start time: 1h 0m 0s
        End time: 2h 30m 30s
        Duration: 1h 30m 30s
        
        Event[1]:
        Start time: 3h 45m 0s
        End time: 5h 0m 0s
        Duration: 2h -45m 0s
        
        Event[2]:
        Start time: 6h 30m 0s
        End time: 8h 45m 30s
        Duration: 2h 15m 30s

## Optional Tasks
The program currently only supports storing events such that the start time minutes and seconds are less than the end time and minutes.

You can identify the flaw in this program by entering the event below:

Event #1
- start time: 5:45:45
- end_time: 6:30:30

This results in the duration of 1h -15m -15s

This is obviously not what we want to happen.

1. Fix the implementation of `print_diff_time` to print the correct duration even in situation outlined above

1. Test your code with inputs for which the previous program failed to compute the correct duration
