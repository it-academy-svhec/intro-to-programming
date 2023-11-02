VA_SALES_TAX = 0.053


def calculate_tax(price, rate):
    return price * rate


def create_items(items):
    item_count = int(input("How many items are you purchasing?"))

    for item in range(item_count):
        name = input("Name: ")
        price = float(input("Price: "))

        new_item = [name, price]

        items.append(new_item)


def print_items(items):
    for item in items:
        item[1] += calculate_tax(item[1], VA_SALES_TAX)
        print(f"Name: {item[0]} | Price: {item[1]}")

items = []

create_items(items)
print_items(items)

create_items(items)
print_items(items)
