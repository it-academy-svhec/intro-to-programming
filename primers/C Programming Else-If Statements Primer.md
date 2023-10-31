# Else-If Statements
Else-if provides a more robust selection structure. It also improves the readability over nested if-else statements. Although braces aren't required for single-statement code blocks, it is preferred by many developers to use them anyway. This makes future updates to source easier. Languages like Python do not use curly braces at all and organization is determined purely by indentation. C does not care about indentation, but it makes your code more readable.

## ATM Scenario
1. Create a Repl named **Else-If Statements Primer**

1. Suppose you are implementing a program for ATM (automated teller machine) such as the user interface below. You are concerned with the logical details rather than the user interface. For your simple program, the system is purely command-line-based.

    ![image](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/71c71c9b-48c4-4984-b329-f5651b537fb3)
   
    **Figure:** [Bank of America ATM User Interface](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FAn-ATM-interface-of-Bank-of-America-showing-some-of-the-offered-services_fig1_294750603&psig=AOvVaw0bxEspOGWNkHMYdnifamC6&ust=1694636422499000&source=images&cd=vfe&opi=89978449&ved=0CBEQjhxqFwoTCJj3peLypYEDFQAAAAAdAAAAABAD)

1. Copy and paste the following source code

    ```C
    #include <stdio.h>

    int main(void) {
    int option;
  
    printf("Please select a menu option.\n1. Withdrawal\n2. Deposit\n3. Balance "
           "Inquiry\n4. Transfer & Payments\n5. Cancel\n");
    scanf("%d", &option);

    if (option == 1) {
      printf("How much would you like to withdrawal?\n");
    } else if (option == 2) {
      printf("How much would you like to deposit?\n");
    } else if (option == 3) {
      printf("Your balance is ? dollars.\n");
    } else if (option == 4) {
      printf("Enter source and destination account info\n");
    } else if (option == 5) {
      printf("Bye. Thanks for banking with us!\n");
    } else {
      printf("'%d' is not a valid option.\nPlease try again.", option);
    }
  
      return 0;
    }
    ```

1. Run the code and test the supported menu options

1. Add a new menu option based on the values below. Move the cancel option down to 6 to make room for this new option

    |Number Option|Name|Message to Print|
    |-|-|-|
    |5|Set preferences|Enter your preferences and press Save|

1. Test your program to ensure the old options still work. Test that the new option is supported.
