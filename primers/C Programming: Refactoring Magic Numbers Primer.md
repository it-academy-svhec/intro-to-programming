## Refactoring Magic Numbers Primer

Refactoring is the process of changing the internal structure of a program while maintaining the same external behavior and functionality. This is necessary to clean up code and make it more accessible to other programmers and yourself in the future. We are going to focus our refactoring efforts on removing magic numbers, which are hardcoded values with a potentially ambiguous purpose throughout our code.

When programmers first define magic numbers, the intention may be clear, but over time they and other programmers are likely to not realize the meaning. Hardcoded values are also inefficient and difficult to update. Instead, it is a best practice to store values of importance in variables and set to be constant if they should be the same throughout the program.

### Refactoring

1. Fork the source code from [Discounts and Sales Tax](https://replit.com/@JacobCook2/Discounts-and-Sales-Tax#main.c) and name it **Refactoring Discounts and Sales Tax**

1. Run the program with two different inputs and record the results. You will use these inputs and outputs to test your code after refactoring since breaking the code is always a risk.

1. Look at the code that creates a constant float variable: `const float DISCOUNT_RATE = 0.10;`. We use the keyword `const` to ensure that the value won't change later in the program. Constants are often named using uppercase with underscores to separate each word.

1. Let's transform the magic number used to check if the total cost is eligible for a discount.

    a. Add the following line of code under the `DISCOUNT_RATE` declaration:

        const float MIN_COST = 100.00;

    b. Replace the hardcoded `100.00` in the if statement condition with the new variable

1. Now, let's do the same for the sales tax value

    a. Add the following line of code next:

        const float VA_SALES_TAX = 0.053;

    b. Replace the hardcoded `0.053` in the sales tax calculation expression with the new variable

### Testing

1. Run the program with the 2 inputs from before and compare the actual output values to the expected results

1. Fix any issues that may arise
