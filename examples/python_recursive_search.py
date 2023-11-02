def search(search_object, target):
    if isinstance(search_object, str):
        return search_object == target
    elif isinstance(search_object, list):
        for item in search_object:
            if search(item, target):
                return True
    return False


my_items = ["Guitar", "Car", "PS5"]
your_items = ["TV", "Bike", "Xbox"]

items = [my_items, your_items]

search_item = input("Enter an item to search for: ")

print("Item found" if search(items, search_item) else "Item not found")
