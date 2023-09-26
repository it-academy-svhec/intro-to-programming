## Advanced Arrays Primer
You will work with pointer variables and arrays. It is essential to understand the concept of pointers to understand how arrays are handled in a program. Then you will practice basic array operations such as accessing data, initializing values, storing data, and passing arrays to functions. 

### Pointer Variables
Pointer variables store the memory address of another variable. This allows us to reference a variable rather than copying its value. Pointer variables also have an associated data type such as `int`, `float`, or `char`, which indicate the data type of the variable referred to by the memory address.

1. Create a new Repl and call it **Advanced Arrays Primer**

1. Enter the following source code. Comments are optional. This code so far will print the memory address where `my_number` is stored in two ways: directly via the address of `my_number` and indirectly via the pointer variable `my_pointer`.

    ```C
    #include <stdio.h>
    
    // Print the hexadecimal memory address where the variable number is stored
    int main(void) {
      int my_number = 0;
      int *my_pointer;
    
      my_pointer = &my_number;
    
      // Using format specifier %p for pointers
      printf("Address of my_number variable: %p\n", &my_number);
      printf("Address of my_pointer variable: %p\n", my_pointer);
    
      return 0;
    }
    ```
    
    We use the `%p` format specifier to properly format pointers as hexadecimal memory addresses. The pointer variable named `my_pointer` stores the memory address of the `my_number` integer variable. The address operator (`&`) returns the memory address of the variable called `my_number`. We do not need to handle memory addresses in such an explicit manner as you will see shortly.

1. Run the program several times and notice how the hex memory addresses printed are different. That is because different blocks of memory are assigned to the `my_number` variable each time you run the program.

### Pass by Value vs. Reference
Functions can be defined and called with or without arguments (actual values passed when a function is called). When passing variables to functions, you must understand if the data is passed as a copy (by value) or as a reference (by the memory address). If the variable is passed by value, changes to the varaible inside the function are scoped locally to that function and do not impact the variable in other scopes outside of the function. If the variable is pased by reference, a `reference` to the original variable (i.e., the hexadecimal memory address) is provided instead. This means that changes to the variable inside the function affect the original variable outside of the function body, or scope.

1. Add the following function declarations above the `main` function

   ```C
   int add_by_copy(int num);
   void add_by_reference(int *num);
   ```

1. Add the following function definitions below (not inside the braces) the `main` function

   ```C
   int add_by_copy(int num) { return num++; }
   void add_by_reference(int *num) { (*num)++; }
   ```

1. Add the following code after the second print statement

    ```C
    printf("Before | Value of my_number: %d\n", my_number);
    
    add_by_reference(my_pointer);
    add_by_copy(my_number);
    
    printf("After | Value of my_number: %d\n", my_number);
    ```
    The `add_by_reference` function receives `my_pointer` as an argument by reference, which is set to the memory address of `my_number`. This allows the function to modify the variable even though it is declared in a different scope. On the other hand, the `add_by_copy` function receives `my_number` as an argument by value (copy). This means that modifications only affect the locally-scoped copy inside the function body.

1. Run the program and notice how `my_number` is only incremented once despite calling `add_by_reference` and `add_by_copy`

### Defining Arrays
```C
/// Array Declaration Syntax
//  <type> <idenifier> [<size>]
```

Arrays are usually declared with a specified length.
```C
// no initializer list, length specifier required!
int numbers[4]; // contains default values {0,0,0,0}
```

However, they may be declared without one, if there is an explicit initialization.
```C
// has initializer list, length specifier is not required.
int numbers[4] = {11,22,33,44};
int numbers[] = {11,22,33,44};
```

1. Clear the current Repl and enter the following source code

    ```C
    #include <stdio.h>
    
    int main(void) {
      // Array
        
      return 0;
    }
    ```

1. Using the examples above, create an array with the following requirements
    - **Identifier**: `user_ids`
    - **Size**: `10`
    - **Initial values**: `1000`, `1001`, `1002`, and `1003`
  
1. Run your program to ensure it is error free

### Storing and Accessing Array Elements
Arrays are indexable containers, meaning they hold 'cells' of data. <br>
These 'cells' are referred to as elements.

An element of an array can be accessed by something called an 'index'. <br>
An index is simply the location of an individual cell inside the array.

```C
// example data

int numbers[4] = {65, 43, 51, 87};
// or
int numbers[] = {65, 43, 51, 87};
```

```C
// Hard-coded Indexing

// easily readable, index values are known
int element2 = numbers[1]; // 43
int element3 = numbers[2]; // 51
```

```C
// Variable Indexing

// some_index_value == ??
// index value is unknown; may have been provided elsewhere in the code
int elementA = numbers[some_index_value]; // value at index
int elementB = numbers[some_index_value + 1]; // value at index + 1
```

1. Write a series of statements to print the values from the `user_ids` using hard-coded indexing

1. Run your program and ensure the output is similar to the following

        User ID: 1000
        User ID: 1001
        User ID: 1002
        User ID: 1003

Now imagine you have 10,000 users. I seriously doubt you would want to write a print statement 10,000 times. This approach is bad for at least two reasons: code duplication and scalability. In the next section, you will implement a more efficient program to print user IDs for an arbitrary number of users.

1. Add the following lines inside the for loop body below the print statement

   ```C
   if (user_ids[index] == 0) {
     char option;
     printf("Do you want to assign the next user ID? (Y or N)\n");
     scanf("%c", &option);
     getchar();
    
     if (option == 'Y') {
       user_ids[index] = user_ids[index == 0 ? 0 : index - 1] + 1;
       printf("User ID: %d assigned\n", user_ids[index]);
     }
   }
   ```

1. Run the program

### Looping Over Arrays
```C
// Array Access (Reading data)
int sum = 0; // variable to hold sum of numbers
const int SIZE = 10; // variable to hold size of the array; i.e., the number of elements
for (int index = 0; index < SIZE; index++) {
    // accessing element at 'index'
    int current_number = numbers[index];
    
    // add the current number to the total
    sum += selected_number;
}
```

```C
// Array Storage (Writing data)
int users_number = 0;
const int SIZE = 10;
for (int index = 0; index < SIZE; index++) {
    // get number from user
    scanf("%d", &users_number);

    // assign new value to element 'index'
    numbers[index] = users_number;
}
```

1. Using the examples above, create a for loop that iterates for each element in the `user_ids` array. Pay close attention to the size of the array.

1. Next, add a print statement inside the for loop body to print the user ID for the current `index` (position).

1. Run your program and ensure the output is similar to the following

        User ID: 1000
        User ID: 1001
        User ID: 1002
        User ID: 1003
        User ID: 0
        User ID: 0
        User ID: 0
        User ID: 0
        User ID: 0
        User ID: 0

Note that the indices (plural for index) that were not explicilty initialized to a user ID are set to 0.

### Using Arrays with Functions
```C
// takes an array of numbers and modifies it
// adds one to each existing element

// ex.  {1,3,5,7} -> {2,4,6,8}

void array_add_one(int length, int numbers[]) {
    for (int i = 0; i < length; i++) {
        numbers[i] += 1;
    }
    // returns nothing
}
```

```C
// takes an array of numbers and a target value
// loops through array to hopefully find the target

// ex.  numbers={4,6,8,10}
//      target=11 -> returns 0
//      target=6 -> returns 1

int array_find_x(int length, int numbers[], int target) {
    for (int i = 0; i < length; i++) {
        int current_number = numbers[i];
        if (current_number == target) {
            // found target
            return 1;
        }
        // target not found, continuing...
    }
    // failed to find target
    return 0;
}
```
