# 🧩 PCEP 4.7 Primer: Python Exceptions

## Part 1: 🌲 **Python Built-In Exceptions Hierarchy** (PCEP-30-02 4.3)

### 1.1 The Big Picture: Exception Hierarchy 🎨

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

🧠 **Quick Tip:**  
Think of this like a family tree — all errors in Python come from `BaseException`.

---

### 1.2 🧩 `BaseException`
- Root of all exceptions.
- Usually **not** caught directly (too broad).

```python
try:
    raise BaseException("Base exception raised")
except BaseException as e:
    print(e)
```

📝 **Try it!**
- Raise and catch a `BaseException`.

---

### 1.3 🎯 `Exception`
- Most exceptions you work with come from here!

```python
try:
    raise Exception("General exception")
except Exception as e:
    print(e)
```

📝 **Try it!**
- Raise and catch an `Exception`.

---

### 1.4 🚪 `SystemExit`
- Raised when Python is asked to exit.

```python
import sys

try:
    sys.exit("Exiting program")
except SystemExit as e:
    print(e)
```

📝 **Try it!**
- Use `sys.exit()` inside a `try-except` block.

🧩 **Did you know?**
- Catching `SystemExit` can be handy for cleanup!

---

### 1.5 ⌨️ `KeyboardInterrupt`
- Happens when you stop the program manually (Ctrl + C).

```python
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted!")
```

📝 **Try it!**
- Run the code and press **Ctrl + C** to stop it.

---

### 1.6 🎓 Abstract Exceptions: Categories

#### 🧮 `ArithmeticError`
- Base class for math errors:
  - `ZeroDivisionError`
  - `OverflowError`

```python
try:
    1 / 0
except ArithmeticError as e:
    print(e)
```

#### 🔍 `LookupError`
- Base class for lookup failures:
  - `IndexError`
  - `KeyError`

---

### 1.7 🧩 `IndexError`

```python
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print(e)
```

📝 **Try it!**
- Access an index out of range.

💡 **Tip:** Happens when you go outside list boundaries.

---

### 1.8 🧩 `KeyError`

```python
my_dict = {"a": 1}
try:
    print(my_dict["b"])
except KeyError as e:
    print(e)
```

📝 **Try it!**
- Access a missing key in your dictionary.

💡 **Tip:** Happens when the key isn't found.

---

### 1.9 🧩 `TypeError`

```python
try:
    "2" + 2
except TypeError as e:
    print(e)
```

📝 **Try it!**
- Try adding a string and an integer.

💡 **Tip:** Python needs matching types!

---

### 1.10 🧩 `ValueError`

```python
try:
    int("hello")
except ValueError as e:
    print(e)
```

📝 **Try it!**
- Convert a non-numeric string to int.

💡 **Tip:** Input looks right type-wise, but value is wrong.

---

## Part 2: 🛠️ **Python Exception Handling Basics** (PCEP-30-02 4.4)

### 2.1 ⚙️ Try-Except Block

```python
try:
    result = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

📝 **Try it!**
- Write your own try-except block!

🧩 **Note:** Always start with `try:`, follow with `except`.

---

### 2.2 🧩 Ordering Except Branches

```python
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index error caught!")
except LookupError:
    print("Lookup error caught!")
```

📝 **Try it!**
- What happens if you switch the order of `IndexError` and `LookupError`?

💡 **Hint:** Python checks from top to bottom!

---

### 2.3 📞 Propagating Exceptions Through Functions

```python
def risky_function():
    return 1 / 0

try:
    risky_function()
except ZeroDivisionError:
    print("Handled in calling code")
```

📝 **Try it!**
- Call a function that raises an error and handle it outside the function.

💡 **Tip:** Errors can travel ("propagate")!

---

### 2.4 🧩 Delegating Responsibility

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

📝 **Try it!**
- Write a function that raises an exception and catch it in a separate function.

💡 **Tip:** Functions can handle their own errors!

---

## 🚀 Challenge Activity!

- Create a program that:
  - Asks the user to enter their age.
  - Converts the input to an integer.
  - If the input is not a number, catch `ValueError` and print an error message.
  - If the age is negative, raise your own `ValueError` with a custom message like *"Age cannot be negative!"*.
  - If everything is correct, print: *"You are X years old!"*

Bonus:  
- Wrap the logic in a function, and call the function inside a `try-except` block to practice propagating exceptions.
