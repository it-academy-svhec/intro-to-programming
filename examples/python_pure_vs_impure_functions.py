total = 0


def pure_add(num1, num2):
    return num1 + num2


def impure_subtotal(price1, price2, price3):
    global total
    total += price1 + price2 + price3

    return total


# Tests
assert pure_add(2, 2) == 4
assert pure_add(2, 2) == 4

assert impure_subtotal(10, 20, 30) == 60
assert impure_subtotal(10, 20, 30) == 60
