## Refactoring Magic Numbers Primer

Refactoring is the process of changing the internal structure of a program while maintaining the same external behavior and functionality. This is necessary to clean up code and make it more accessible to other programmers and yourself in the future. We are going to focus our refactoring efforts on removing magic numbers, which are hardcoded values with a potentially ambiguous purpose throughout our code.

When programmers first define magic numbers, the intention may be clear, but over time they and other programmers are likely to not realize the meaning. Hardcoded values are also inefficient and difficult to update. Instead, it is a best practice to store values of importance in variables and set to be constant if they should be the same throughout the program.

### Refactoring

1. Create a new Repl and call it **Refactoring Discounts and Sales Tax**
1. Develop 2 scenarios for input and expected output. This will help to ensure that refactoring doesn't break your already working code.
1. Look at the code that creates a constant float variable: `const float DISCOUNT_RATE = 0.10;`. We use the keyword `const` to ensure that the value won't change later in the program. Constants are often named using uppercase with underscores to separate each word.
1. Let's transform the magic number used to check if the total cost is eligible for a discount.

    a. Add the following line of code under the `DISCOUNT_RATE` declaration:

   const float MIN_COST = 100.00;

    a. Replace the hardcoded `100.00` in the if statement condition with the new variable

1. Now, let's do the same for the sales tax value
  a. Add the following line of code next:

    const float VA_SALES_TAX = 0.053;

  a. Replace the hardcoded `0.053` in the sales tax calculation expression with the new variable
