Of course! Here’s your primer in clean, student-friendly **Markdown** format:

---

# 🧩 PCEP Primer: Tuples & Dictionaries (Hands-On)

## Part 1: **Tuples** (PCEP-30-02 3.2)

### 1.1 What is a Tuple?
- A **tuple** is an ordered collection of items.
- It is **immutable**, meaning once created, you cannot change its contents.

```python
my_tuple = (10, 20, 30, 40)
print(my_tuple)
```

**📝 Try it!**
- Create a tuple with 4 different fruits.
- Print the second item.

---

### 1.2 Indexing and Slicing

```python
print(my_tuple[1])  # Indexing (starts at 0)
print(my_tuple[1:3])  # Slicing
```

**📝 Try it!**
- Slice the last two items from your fruit tuple.

---

### 1.3 Building Tuples
- You can build tuples from existing lists or directly:

```python
numbers = tuple([1, 2, 3])
empty_tuple = ()
single_item_tuple = (42,)  # Note the comma!
```

**📝 Try it!**
- Convert a list of colors to a tuple.

---

### 1.4 Immutability

```python
my_tuple[0] = 99  # ❌ This will give an error!
```

**📝 Try it!**
- Try to change an item in your tuple. What error do you get?

---

### 1.5 Tuples vs Lists

| Feature               | Tuple            | List           |
|----------------------|------------------|----------------|
| Mutable?             | ❌ No            | ✅ Yes         |
| Syntax               | `(1, 2, 3)`      | `[1, 2, 3]`    |
| Faster performance   | ✅ Usually       | ❌ Slower      |
| Nesting allowed?     | ✅ Yes           | ✅ Yes         |

**📝 Try it!**
- Create a list inside a tuple: `mixed = ([1, 2], 'hello')`
- Access the list and add an item to it.

---

### 1.6 Lists inside Tuples and Tuples inside Lists

```python
tuple_with_list = (1, [2, 3], 4)
list_with_tuple = [("a", "b"), ("c", "d")]
```

**📝 Try it!**
- Access the nested list in `tuple_with_list` and append a new number.

---

## Part 2: **Dictionaries** (PCEP-30-02 3.3)

### 2.1 What is a Dictionary?
- A **dictionary** stores data as key-value pairs.

```python
student = {"name": "Alice", "age": 25}
print(student)
```

**📝 Try it!**
- Create a dictionary for your favorite book with keys: `title`, `author`, `year`.

---

### 2.2 Indexing, Adding, and Removing Keys

```python
# Accessing
print(student["name"])

# Adding
student["grade"] = "A"

# Removing
del student["age"]
```

**📝 Try it!**
- Add a new key `"pages"` to your book dictionary.
- Remove the `"year"` key.

---

### 2.3 Iterating Through Dictionaries

```python
for key in student:
    print(key, student[key])
```

**📝 Try it!**
- Loop through your book dictionary and print keys and values.

---

### 2.4 Checking Existence of Keys

```python
if "grade" in student:
    print("Grade exists!")
```

**📝 Try it!**
- Check if the key `"author"` exists in your book dictionary.

---

### 2.5 Dictionary Methods: `keys()`, `items()`, `values()`

```python
print(student.keys())    # Keys
print(student.values())  # Values
print(student.items())   # Key-value pairs
```

**📝 Try it!**
- Print just the values of your dictionary.
- Print both keys and values using `.items()`.

---

## 🚀 Challenge Activity!
- Build a dictionary for **3 students**, where each student has:
  - Name
  - Age
  - List of grades
- Print out:
  - Each student’s name
  - Their list of grades
  - Average of grades (hint: use `sum()` and `len()`)
