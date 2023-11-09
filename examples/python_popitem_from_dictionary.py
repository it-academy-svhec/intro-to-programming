waiting_line = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3,
    "David": 4,
    "Eva": 5
}

print("Initial Waiting Line:", waiting_line)

while waiting_line:
    name, position = waiting_line.popitem()
    print(f"Serving {name} (Position: {position})")

print("Updated Waiting Line:", waiting_line)
