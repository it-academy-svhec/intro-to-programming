# Python 2.3 - 2.6 Primer

Welcome to this interactive Python primer! Throughout this guide, you will learn Python fundamentals by trying out code snippets and answering questions along the way. Let's get started!

---

## Operators in Python
Operators in Python allow you to perform operations on variables and values. Try out the examples in a Python environment!

### Arithmetic Operators
Let's start with some basic math.

For each of the following examples, predict the output, run the code, and compare your expected result to the actual result.
```python
print(5 + 3)  # Try this!
print(10 - 4)
print(6 * 2)
print(9 / 3)
print(10 // 3)
print(10 % 3)
print(2 ** 3)
```
Now, modify the code above and experiment with different numbers!

### Comparison Operators
Predict whether each statement below will print `True` or `False`. Then run the code to check your answers!
```python
x = 7
y = 4
print(x > y)
print(x == y)
print(x != y)
```
Now, change the values of `x` and `y` and see what happens.

### Logical Operators
Try to guess the output before running this code:
```python
x = True
y = False
print(x and y)
print(x or y)
print(not x)
```
Can you modify the values of `x` and `y` to get different results?

### Assignment Operators
Try this code and observe how the variable `x` changes:
```python
x = 5
x += 3
print(x)  # What will this print?
```
Now, experiment with `-=` and `*=`.

---

## Variables in Python
Variables store values. Try running this:
```python
name = "Alice"
age = 25
height = 5.9
is_student = True
print(name, age, height, is_student)
```
Now, change the values of these variables and see how it affects the output.

### Challenge: Create Your Own Variables
Write a Python script that defines three variables of different types and prints them. Be creative!

---

## Comments in Python
Comments help explain the code. Run the code below and notice that comments do not affect execution.
```python
# This is a single-line comment
x = 5  # Assigning 5 to x
print(x)
```
Try writing a multi-line comment describing what this program does:
```python
"""
Your comment here!
"""
print("Python is fun!")
```

---

## User Interaction in Python
### Taking User Input
Run this script and enter your name when prompted:
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```
Now, modify it to ask for the user’s age and print a message including both name and age.

### Input as Numbers
Modify this program to allow the user to enter two numbers and display their sum:
```python
num = int(input("Enter a number: "))
print("Twice your number is", num * 2)
```

### Formatting Output
Try this:
```python
name = "Alice"
age = 25
print(f"{name} is {age} years old.")
```
Can you modify it to include a favorite hobby as well?

---

### Final Challenge
Create a Python script that asks for a user’s name, favorite color, and favorite number, then prints a formatted sentence using this information. Test it out and make it your own!

Congratulations! You've completed this interactive primer. Keep practicing and experimenting with Python!
