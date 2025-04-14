# 🧩 PCEP Primer: Tuples & Dictionaries (Hands-On, Deep Dive)

---

## Part 1: **Tuples** (PCEP-30-02 3.2)

### 1.1 What is a Tuple?
- A **tuple** is an **ordered**, **immutable** collection.
- Useful when you want to group related values that should not change.
- Immutable = *"set in stone"* (you can't add, remove, or change elements).

```python
my_tuple = (10, 20, 30, 40)
print(my_tuple)
```

**📝 Try it!**
- Create a tuple with 4 different fruits.
- Print the second item.

**💡 Why use a tuple?**  
- Protect data from accidental changes.
- Tuples are faster than lists (Python optimizes them).

---

### 1.2 Indexing and Slicing
- Tuples use **zero-based indexing**.
- Slicing creates a new tuple of selected items.

```python
print(my_tuple[1])  # Indexing
print(my_tuple[1:3])  # Slicing
```

**📝 Try it!**
- Slice the last two items from your fruit tuple.

**🚧 Common mistake:**  
Don’t forget: slicing **includes the start index but excludes the end**.

---

### 1.3 Building Tuples
- Convert other collections to tuples:
  
```python
colors_list = ["red", "green", "blue"]
colors_tuple = tuple(colors_list)
print(colors_tuple)
```

- Special case: **single-item tuple** needs a comma!
  
```python
single = (42,)  # ← comma is important!
```

**📝 Try it!**
- Convert a list of colors to a tuple.
- Make a single-item tuple and print its type with `type()`.

---

### 1.4 Immutability
```python
my_tuple[0] = 99  # ❌ Error!
```

**📝 Try it!**
- Try to change an item in your tuple. What error do you get?

**💡 Note:**  
While tuples are immutable, if they contain **mutable objects** (like lists), those objects can change!

---

### 1.5 Tuples vs Lists: When to use?

| Feature               | Tuple            | List           |
|----------------------|------------------|----------------|
| Mutable?             | ❌ No            | ✅ Yes         |
| Syntax               | `(1, 2, 3)`      | `[1, 2, 3]`    |
| Faster performance   | ✅ Usually       | ❌ Slower      |
| Nesting allowed?     | ✅ Yes           | ✅ Yes         |
| Use case             | Fixed data       | Dynamic data   |

**📝 Try it!**
- Create a tuple with a list inside it.
- Add an item to the list inside the tuple.

**🚀 Bonus:**  
- What happens if you try to change the tuple itself? Test it!

---

### 1.6 Lists inside Tuples and Tuples inside Lists

```python
tuple_with_list = (1, [2, 3], 4)
list_with_tuple = [("a", "b"), ("c", "d")]
```

**📝 Try it!**
- Access the nested list in `tuple_with_list` and append a number.
- Print the modified tuple.

**💡 Insight:**  
Tuples provide structure, but they can still hold changeable data.

---

## Part 2: **Dictionaries** (PCEP-30-02 3.3)

### 2.1 What is a Dictionary?
- Think of it like a **real dictionary**: words (keys) → meanings (values).
- Stores **key-value** pairs.
- **Keys are unique and immutable** (numbers, strings, tuples).

```python
student = {"name": "Alice", "age": 25}
print(student)
```

**📝 Try it!**
- Create a dictionary for your favorite book with keys: `title`, `author`, `year`.

**💡 Memory trick:**  
- Dictionary = **unordered (before Python 3.7) → ordered (from Python 3.7+)**

---

### 2.2 Accessing, Adding, and Removing Keys

```python
print(student["name"])  # Accessing

student["grade"] = "A"  # Adding

del student["age"]  # Removing
```

**📝 Try it!**
- Add `"pages"` to your book dictionary.
- Remove the `"year"` key.

**🚧 Common mistake:**  
Accessing a non-existent key with `student["height"]` will throw an error. Use `.get()` to avoid this!

---

### 2.3 Iterating Through Dictionaries

```python
for key in student:
    print(key, student[key])
```

**📝 Try it!**
- Loop through your book dictionary and print keys and values.

**🚀 Bonus:**  
- Print only the values.
- Print formatted: `Key: name → Value: Alice`

---

### 2.4 Checking Existence of Keys

```python
if "grade" in student:
    print("Grade exists!")
```

**📝 Try it!**
- Check if `"author"` exists in your book dictionary.

**🚧 Tip:**  
Use `in` to avoid KeyError!

---

### 2.5 Dictionary Methods: `.keys()`, `.items()`, `.values()`

```python
print(student.keys())    # Keys
print(student.values())  # Values
print(student.items())   # Key-value pairs
```

**📝 Try it!**
- Print just the values of your dictionary.
- Print both keys and values using `.items()`.

**💡 Extra:**  
Wrap with `list()` to see as a list: `list(student.keys())`

---

## 🚀 Challenge Activity: Student Directory

Build a dictionary for **3 students**:
```python
students = {
    "student1": {"name": "Alice", "age": 20, "grades": [90, 85, 92]},
    "student2": {"name": "Bob", "age": 22, "grades": [78, 81, 86]},
    "student3": {"name": "Charlie", "age": 19, "grades": [95, 89, 94]},
}
```

Print:
- Each student’s name
- Their list of grades
- The average grade (use `sum()` and `len()`)

**📝 Try it!**
- Can you extend it to count how many students scored above 90 average?

---

## 🌟 Bonus Section: Nested Dictionaries
- Dictionaries can hold dictionaries!

```python
school = {
    "Class A": {"teacher": "Ms. Smith", "students": 25},
    "Class B": {"teacher": "Mr. Lee", "students": 20}
}
```

**📝 Try it!**
- Print the teacher of "Class A".
