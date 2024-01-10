# Arrays Primer

Arrays are used to store more than 1 value of the same data type. For example, arrays in C can be used to store a list of email addresses or phone numbers. Arrays are very important but have some nuances.

## Basic Array Usage

1. Create a new Repl and call it **Arrays Primer**

1. Enter the following source code:

   ```C
   #include <stdio.h>

   int main() {
     int digits[3];

     return 0;
   }
   ```

   This array is declared and initialized to store up to 3 elements of the type integer. Memory is reserved by the program when this array is initialized.
   The array index starts at 0 and you can use the `[]` notation to store or retrieve an element in an array.

1. Let's store the number `7` at position `0`, the first position, in the array. Add the following code under the declaration of the array.

   ```C
   digits[0] = 7;
   ```

1. Store numbers in the remaining two positions at index `1` and then `2`

1. Add the following print statement to print the value of the element at array index `0`, the first element. Place this after storing values in the array.

   ```C
   printf("%d\n", digits[0]);
   ```

   `%d` tells C to format the output as a decimal integer. `\n` appends a newline character to the output.

1. Add print statements for the array elements at index `1` and `2` also
