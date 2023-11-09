import copy

def subtotal_items_with_discount(items, discount):
    # Slice copy of the list
    copy_items = copy.deepcopy(items)
    subtotal = 0.0

    for item in copy_items:
        item[1] *= 1 - discount
        subtotal += item[1]
        print(f"Name: {item[0]} | Price: ${item[1]}")

    print(f"Subtotal: ${subtotal}")


items = [["Guitar", 500], ["Car", 1000]]

BLACK_FRIDAY_RATE = 0.10

subtotal_items_with_discount(items, BLACK_FRIDAY_RATE)

# Ensure data was not mutated
assert items[0][0] == "Guitar"
assert items[0][1] == 500

assert items[1][0] == "Car"
assert items[1][1] == 1000
