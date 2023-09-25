## Advanced Arrays Primer
TODO: high-level overview

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
    
    We use the `%p` format specifier to properly format pointers as hexadecimal memory addresses. The pointer variable named `my_pointer` stores the memory address of the `my_number` integer variable. The address operator (`&`) returns the memory address of the variable called `my_number`.

1. 
