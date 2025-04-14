Of course! Here’s your second **primer** in clean, student-friendly **Markdown**, following the same format:

---

# 🧩 PCEP Primer: Python Exceptions (Hands-On)

## Part 1: **Python Built-In Exceptions Hierarchy** (PCEP-30-02 4.3)

### 1.1 The Big Picture: Exception Hierarchy

At the top:
```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    ├── LookupError
        ├── IndexError
        └── KeyError
    ├── TypeError
    └── ValueError
```

---

### 1.2 `BaseException`
- Root of all exceptions.
- Usually not caught directly.

```python
try:
    raise BaseException("Base exception raised")
except BaseException as e:
    print(e)
```

**📝 Try it!**
- Raise and catch a `BaseException`.

---

### 1.3 `Exception`
- Most user-defined exceptions derive from `Exception`.

```python
try:
    raise Exception("General exception")
except Exception as e:
    print(e)
```

**📝 Try it!**
- Raise and catch an `Exception`.

---

### 1.4 `SystemExit`
- Raised by `sys.exit()`.
- Stops the program.

```python
import sys

try:
    sys.exit("Exiting program")
except SystemExit as e:
    print(e)
```

**📝 Try it!**
- Use `sys.exit()` inside a `try-except` block.

---

### 1.5 `KeyboardInterrupt`
- Triggered when you interrupt the program manually (like `Ctrl + C`).

```python
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted!")
```

**📝 Try it!**
- Run the code and press `Ctrl + C` to stop it.

---

### 1.6 Abstract Exceptions: Categories

#### `ArithmeticError`
- Base class for math errors like:
  - `ZeroDivisionError`
  - `OverflowError`

```python
try:
    1 / 0
except ArithmeticError as e:
    print(e)
```

#### `LookupError`
- Base class for lookup failures:
  - `IndexError`
  - `KeyError`

---

### 1.7 `IndexError`

```python
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print(e)
```

**📝 Try it!**
- Access an index out of range.

---

### 1.8 `KeyError`

```python
my_dict = {"a": 1}
try:
    print(my_dict["b"])
except KeyError as e:
    print(e)
```

**📝 Try it!**
- Try accessing a missing key in your dictionary.

---

### 1.9 `TypeError`

```python
try:
    "2" + 2
except TypeError as e:
    print(e)
```

**📝 Try it!**
- Try to add a string and an integer.

---

### 1.10 `ValueError`

```python
try:
    int("hello")
except ValueError as e:
    print(e)
```

**📝 Try it!**
- Convert a non-numeric string to int.

---

## Part 2: **Python Exception Handling Basics** (PCEP-30-02 4.4)

### 2.1 Try-Except Block

```python
try:
    result = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**📝 Try it!**
- Write your own try-except block!

---

### 2.2 Ordering Except Branches

```python
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index error caught!")
except LookupError:
    print("Lookup error caught!")
```

**📝 Try it!**
- What happens if you switch the order of `IndexError` and `LookupError`?

---

### 2.3 Propagating Exceptions Through Functions

```python
def risky_function():
    return 1 / 0

try:
    risky_function()
except ZeroDivisionError:
    print("Handled in calling code")
```

**📝 Try it!**
- Call a function that raises an error and handle it outside the function.

---

### 2.4 Delegating Responsibility

```python
def risky_function():
    raise ValueError("Oops!")

def handler():
    try:
        risky_function()
    except ValueError as e:
        print(f"Caught inside handler: {e}")

handler()
```

**📝 Try it!**
- Write a function that raises an exception and catch it in a separate function.

---

## 🚀 Challenge Activity!
- Create a program that:
  - Asks the user to input two numbers.
  - Catches `ValueError` if the input is not a number.
  - Catches `ZeroDivisionError` if the user tries to divide by zero.
  - Print a success message if no exceptions occur.
