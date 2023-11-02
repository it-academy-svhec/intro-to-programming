def calculate_discount(customer_type):
    def regular_discount(amount):
        return amount * 0.1

    def premium_discount(amount):
        return amount * 0.2

    def vip_discount(amount):
        return amount * 0.3

    def unknown_discount(amount):
        return 0

    discounts = {
        "regular": regular_discount,
        "premium": premium_discount,
        "vip": vip_discount
    }

    discount_function = discounts.get(customer_type, unknown_discount)

    return discount_function


customer_type = "premium"
purchase_amount = 1000
discount_function = calculate_discount(customer_type)
discount_amount = discount_function(purchase_amount)
final_price = purchase_amount - discount_amount

print(f"Customer Type: {customer_type}")
print(f"Purchase Amount: ${purchase_amount}")
print(f"Discount Amount: ${discount_amount}")
print(f"Final Price: ${final_price}")
