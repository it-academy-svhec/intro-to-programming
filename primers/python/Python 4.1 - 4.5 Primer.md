# Modules 4.1 - 4.5 Primer

When writing programs, it’s important to break your code into smaller, manageable pieces.  
Functions help you:
- Avoid repeating yourself (DRY principle: *Don't Repeat Yourself*)
- Make your code easier to read and understand
- Simplify debugging and testing

Let's go step by step.

---

## 1. Defining Functions

A function is like a mini-program inside your program.  
You define it once, and you can use (or "call") it whenever you need.

### Syntax:
```python
def function_name():
    # Code block (this is the body of the function)
    print("Hello!")
```

### Try it!
On your system, create a Python file (e.g., `functions_intro.py`) and add this function. Then, run it!

### Example:
```python
def greet():
    print("Hello, world!")
```

---

## 2. Invoking (Calling) Functions

Once a function is defined, you can run it by **calling** it by name, followed by parentheses `()`.

```python
greet()  # Output: Hello, world!
```

### Try it!
Add the `greet()` function call below your function definition and run your script.

---

## 3. Functions with Parameters

Functions can take **parameters** — values you provide when calling the function.

### Example:
```python
def greet(name):
    print("Hello,", name)

greet("Alice")  # Output: Hello, Alice
greet("Bob")    # Output: Hello, Bob
```

### Try it!
Update your `greet()` function to take a name parameter and call it with your name.

You can have more than one parameter:
```python
def add(a, b):
    print(a + b)

add(3, 4)  # Output: 7
```

Try calling `add()` with different numbers!

---

## 4. The `return` Keyword

Sometimes, you want your function to give back a value.

Use the `return` keyword to send a result back to the caller.

### Example:
```python
def add(a, b):
    return a + b

result = add(5, 7)
print(result)  # Output: 12
```

### Try it!
Modify the `add()` function to return the result and print it from outside the function.

**Note:**
- When Python hits `return`, it **exits the function immediately**.

---

## 5. The `None` Keyword

If a function doesn’t return anything, Python automatically returns `None`.

### Example:
```python
def say_hello():
    print("Hello!")

result = say_hello()
print(result)  # Output:
# Hello!
# None
```

### Try it!
Run this example and see how `None` appears in the output.

You can also return `None` explicitly:
```python
def check_number(n):
    if n > 0:
        return "Positive"
    else:
        return None

print(check_number(5))   # Output: Positive
print(check_number(-2))  # Output: None
```

Try modifying this function to check for zero as well!

---

## 6. Recursion

A function can call **itself** — this is called **recursion**.

Recursion is useful for problems that can be broken down into smaller, similar problems.

### Example: Factorial
Factorial of `n` (written `n!`) means:  
`n * (n-1) * (n-2) * ... * 1`

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Try it!
Run the factorial example and change the input to different numbers. Try `factorial(3)` or `factorial(6)`.

**Important:**  
Always make sure there’s a base case! Without it, your function will run forever and cause a stack overflow error.

---

## Challenge: Countdown Timer Function

Write a function that counts down from a given number to zero, printing each number along the way.

### Instructions:
1. Define a function called `countdown` that takes one parameter.
2. Use a loop (like `while` or `for`) inside the function to count down from the number to zero.
3. Print each number during the countdown.
4. After reaching zero, print `"Blast off!"`.

### Hint:
```python
def countdown(number):
    while number > 0:
        print(number)
        number -= 1
    print("Blast off!")

countdown(5)
```

**Extra Challenge:** Can you create a **recursive** version of this countdown function?

---

## Quick Summary Table

| Concept | Syntax/Example | Purpose |
|---------|---------------|----------|
| **Define a function** | `def greet():` | Create reusable code blocks |
| **Call a function** | `greet()` | Run the function code |
| **Parameters** | `def greet(name):` | Pass data into functions |
| **Return values** | `return a + b` | Send data back from the function |
| **None keyword** | `return None` or no return | Default return value |
| **Recursion** | `factorial(n)` calls itself | Solve complex problems by breaking them down |
| **Common Mistakes** | Forgetting () when calling functions, missing return, infinite loops. | Common beginner errors to watch out for |

---

## Common Mistakes to Avoid

1. **Forgetting parentheses when calling a function:**
   ```python
   greet  # Does nothing
   greet()  # Correct: calls the function
   ```

2. **Missing a `return` statement when you expect a value:**
   ```python
   def add(a, b):
       sum = a + b  # No return!

   result = add(2, 3)
   print(result)  # Output: None
   ```

3. **Infinite recursion (missing base case):**
   ```python
   def recurse():
       return recurse()  # No base case! Will crash
   ```

4. **Mismatched number of arguments:**
   ```python
   def greet(name):
       print("Hello", name)

   greet()  # Error: missing required argument
   ```

5. **Indentation errors inside functions:**
   ```python
   def greet():
   print("Hello")  # Error: expected an indented block
   ```

---

Happy coding! 🚀
